package com.ilbdaicnl.storm;

import org.apache.storm.utils.Utils;

import com.ilbdaicnl.resources.ResourceMgr;

import java.util.ArrayList;
import java.util.List;

import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.topology.TopologyBuilder;

public class TwitterStreamTopology {
	public static void main(String[] args) {		
        String consumerKey = "";
        String consumerSecret = "";
        String accessToken = "";
        String accessTokenSecret = "";
        List<String> keyWords = new ArrayList<String>();
        
        ResourceMgr resourceMgr = ResourceMgr.getInstance();
        
        consumerKey = resourceMgr.getConsumerKey();
        consumerSecret = resourceMgr.getConsumerSecret();
        accessToken = resourceMgr.getAccessToken();
        accessTokenSecret = resourceMgr.getAccessTokenSecret();
        keyWords = resourceMgr.getKeyWords();
        
        TopologyBuilder builder = new TopologyBuilder();

        builder.setSpout("twitter", new TwitterStreamSpout(consumerKey, consumerSecret,
                accessToken, accessTokenSecret, keyWords.toArray(new String[0])));
        builder.setBolt("formatter", new TweetFormatterBolt()).shuffleGrouping("twitter");
        builder.setBolt("geolocation", new GeolocationBolt()).shuffleGrouping("formatter");
        builder.setBolt("sentiment", new SentimentAnalysisBolt(), 1).shuffleGrouping("geolocation", "success");
        builder.setBolt("print", new TwitterStreamPrint()).shuffleGrouping("insert");
        builder.setBolt("insert", new CassandraInsertBolt()).shuffleGrouping("sentiment");
//        builder.setBolt("log", new LoggerBolt()).shuffleGrouping("insert", "error");


        Config conf = new Config();


        LocalCluster cluster = new LocalCluster();

        cluster.submitTopology("racialMapping", conf, builder.createTopology());

    }
}
