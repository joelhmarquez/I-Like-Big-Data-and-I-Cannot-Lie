package com.ilbdaicnl.storm;

import sun.misc.BASE64Encoder;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Map;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.storm.Config;
import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichSpout;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.utils.Utils;

@SuppressWarnings("serial")
public class TwitterStreamSpout extends BaseRichSpout {
	SpoutOutputCollector _collector;
    LinkedBlockingQueue<String> queue = null;
    String gnipUser;
    String gnipPass;
    String gnipUrl;
    String resp;
    String next = null;
        
    private HttpURLConnection connection = null;
    private InputStream inputStream = null;
    private BufferedReader reader = null;
    

    public TwitterStreamSpout(String gnipUser, String gnipPass, String gnipUrl) {
        this.gnipUser = gnipUser;
        this.gnipPass = gnipPass;
        this.gnipUrl = gnipUrl;
    }

    public TwitterStreamSpout() {
        // TODO Auto-generated constructor stub
    }

    @Override
    public void open(Map conf, TopologyContext context,
                     SpoutOutputCollector collector) {
        _collector = collector;
        queue = new LinkedBlockingQueue<String>(1000);
       
        next = sendRequest(next);
    }	
    
    @Override
    public void deactivate() {
      try {
    	  inputStream.close();
      } catch (IOException e) {
    	  e.printStackTrace();
      }
    }
    @Override
    public void nextTuple() {
    	if(queue.isEmpty())next = sendRequest(next);
    	String ret = queue.poll();
    	if(ret == null){
    		Utils.sleep(50);
    	} else {
    		_collector.emit(new Values(ret));
    		Utils.sleep(15);
    	}
    }

    @Override
    public void close() {
    }

    @Override
    public Map<String, Object> getComponentConfiguration() {
        Config ret = new Config();
        ret.setMaxTaskParallelism(1);
        return ret;
    }

    @Override
    public void ack(Object id) {
    }

    @Override
    public void fail(Object id) {
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("tweet"));
    }
    
   /* GNIP FUNCTIONS */
    
    private String sendRequest(String next){
    	String query = "-0 (has:geo OR has:profile_geo) lang:en";
        String charset = "UTF-8";
        String nextKey = null;
        String queryString = (next==null)? "%s?query=%s&maxResults=500" : "%s?query=%s&maxResults=500&next=" + next;

        	try {
    			String queryURL = String.format(queryString, gnipUrl, java.net.URLEncoder.encode(query, charset));

    	        try {
    	            connection = getConnection(queryURL, gnipUser, gnipPass);

    	            inputStream = connection.getInputStream();
    	            int responseCode = connection.getResponseCode();

    	            if (responseCode >= 200 && responseCode <= 299) {
    	                reader = new BufferedReader(new InputStreamReader((inputStream), charset));
    	                String line = reader.readLine();
    	                while(line != null){
    	                    resp = resp + line;
    	                    line = reader.readLine();
    	                }
    	                Matcher m = Pattern.compile("(\\{\"id\":\"tag.+?\\})(?=,\\{\"id\":\"tag)").matcher(resp);
    	                while(m.find()){
    	                	queue.offer(m.group());
    	                }
    	                Matcher n = Pattern.compile("(?=\"next\":\")(.+?(?=\",\"requestParameters\":))").matcher(resp);
    	                while(n.find()){
    	                	nextKey = n.group(1).substring(8);
    	                } 
    	                System.out.println("API Called with next token: " + next);
    	            } else {
    	                handleNonSuccessResponse(connection);
    	            }
    	        } catch (Exception e) {
    	            e.printStackTrace();
    	            if (connection != null) {
    	                try {
    						handleNonSuccessResponse(connection);
    					} catch (IOException e1) {
    						e1.printStackTrace();
    					}
    	            }
    	        }
    		} catch (UnsupportedEncodingException e2) {
    			e2.printStackTrace();
    		}
        	
        	return nextKey;
    }
    
    private static void handleNonSuccessResponse(HttpURLConnection connection) throws IOException {
        int responseCode = connection.getResponseCode();
        String responseMessage = connection.getResponseMessage();
        System.out.println("Non-success response: " + responseCode + " -- " + responseMessage);
    }

    private static HttpURLConnection getConnection(String urlString, String username, String password) throws IOException {
        URL url = new URL(urlString);

        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setReadTimeout(1000 * 60 * 60);
        connection.setConnectTimeout(1000 * 10);

        connection.setRequestProperty("Authorization", createAuthHeader(username, password));

   return connection;
    }

    private static String createAuthHeader(String username, String password) throws UnsupportedEncodingException {
        BASE64Encoder encoder = new BASE64Encoder();
        String authToken = username + ":" + password;
        return "Basic " + encoder.encode(authToken.getBytes());
    }
}
