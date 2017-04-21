package com.ilbdaicnl.storm;

import com.ilbdaicnl.resources.ResourceMgr;


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

        builder.setSpout("twitter", new TwitterStreamSpout(gnipUser, gnipPass, gnipUrl));
        builder.setBolt("formatter", new TweetFormatterBolt()).shuffleGrouping("twitter");
        builder.setBolt("sentiment", new SentimentAnalysisBolt()).shuffleGrouping("formatter");
        builder.setBolt("insert", new CassandraInsertBolt()).shuffleGrouping("sentiment");
//        builder.setBolt("log", new LoggerBolt()).shuffleGrouping("insert", "error");
        builder.setBolt("print", new TwitterStreamPrint()).shuffleGrouping("insert");


        Config conf = new Config();


        LocalCluster cluster = new LocalCluster();

        cluster.submitTopology("racialMapping", conf, builder.createTopology());

    }
}
