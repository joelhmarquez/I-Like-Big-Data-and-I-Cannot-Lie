package com.ilbdaicnl.storm;

import org.apache.storm.utils.Utils;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

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
        
        /* Reading in twitter oauth values */
        try {
        	Properties env = new Properties();
            InputStream stream = Thread.currentThread().getContextClassLoader().getResourceAsStream("config.properties");
			env.load(stream);
			consumerKey = env.getProperty("consumer.key");
			consumerSecret = env.getProperty("consumer.secret");
			accessToken = env.getProperty("access.token");
			accessTokenSecret = env.getProperty("access.token.secret");
		} catch (IOException e) {
			e.printStackTrace();
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
