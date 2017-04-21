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
        String gnipUser = "";
        String gnipPass = "";
        String gnipUrl = "";
        
        ResourceMgr resourceMgr = ResourceMgr.getInstance();
        
        gnipUser = resourceMgr.getGnipUsername();
        gnipPass = resourceMgr.getGnipPassword();
        gnipUrl = resourceMgr.getGnipUrl();
        
        TopologyBuilder builder = new TopologyBuilder();

        builder.setSpout("twitter", new TwitterStreamSpout2(gnipUser, gnipPass, gnipUrl));
        builder.setBolt("formatter", new TweetFormatterBolt()).shuffleGrouping("twitter");
//        builder.setBolt("sentiment", new SentimentAnalysisBolt()).shuffleGrouping("geolocation", "success");
//        builder.setBolt("print", new TwitterStreamPrint()).shuffleGrouping("geolocation", "failure");
//        builder.setBolt("insert", new CassandraInsertBolt()).shuffleGrouping("sentiment");
//        builder.setBolt("log", new LoggerBolt()).shuffleGrouping("insert", "error");
        builder.setBolt("print", new TwitterStreamPrint()).shuffleGrouping("formatter");


        Config conf = new Config();


        LocalCluster cluster = new LocalCluster();

        cluster.submitTopology("racialMapping", conf, builder.createTopology());

    }
}
