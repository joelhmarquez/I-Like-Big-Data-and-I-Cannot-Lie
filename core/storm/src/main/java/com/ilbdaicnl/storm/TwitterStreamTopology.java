package com.ilbdaicnl.storm;

import org.apache.storm.utils.Utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Locale;
import java.util.ResourceBundle;

import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.topology.TopologyBuilder;

public class TwitterStreamTopology {
	public static void main(String[] args) {
        String consumerKey = "";
        String consumerSecret = "";
        String accessToken = "";
        String accessTokenSecret = "";
        String[] keyWords = {""};
        
        /* Reading in oauth values */
        BufferedReader br = null;
        try {
        	br = new BufferedReader(new FileReader(".env"));
        	
        	consumerKey = br.readLine();
        	consumerSecret = br.readLine();
        	accessToken = br.readLine();
        	accessTokenSecret = br.readLine();
        } catch (IOException ioe) {
        	ioe.printStackTrace();
        } finally {
        	try {
        		if(br != null){
            		br.close();
            	}
        	} catch (IOException ioe){
        		System.out.println("Error in closing the BufferedReader");
        	}
        	
        }
        
        TopologyBuilder builder = new TopologyBuilder();

        builder.setSpout("twitter", new TwitterStreamSpout(consumerKey, consumerSecret,
                accessToken, accessTokenSecret, keyWords));
        builder.setBolt("formatter", new TweetFormatterBolt()).shuffleGrouping("twitter");
        builder.setBolt("geolocation", new GeolocationBolt()).shuffleGrouping("formatter");
//        builder.setBolt("sentiment", new SentimentAnalysisBolt(), 1).shuffleGrouping("twitter");
        builder.setBolt("print", new TwitterStreamPrint()).shuffleGrouping("geolocation");


        Config conf = new Config();


        LocalCluster cluster = new LocalCluster();

        cluster.submitTopology("racialMapping", conf, builder.createTopology());

        Utils.sleep(1000000);
        cluster.shutdown();
    }
}
