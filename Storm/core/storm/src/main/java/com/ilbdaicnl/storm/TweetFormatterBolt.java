package com.ilbdaicnl.storm;

import java.io.IOException;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.ilbdaicnl.resources.TweetObject;


public class TweetFormatterBolt extends BaseBasicBolt {
	@Override
    public void execute(Tuple tuple, BasicOutputCollector collector) {
		ObjectMapper m = new ObjectMapper();
		try {
			JsonNode tweetJson = m.readTree(tuple.getValueByField("tweet").toString());
			TweetObject tweet = new TweetObject(tweetJson);
			if(tweet.getState() != null){
				//System.out.print("Formatted Tweet:" + tweet);
				collector.emit(new Values(tweet.asJSON()));
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}
	}
	
    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
    	declarer.declare(new Fields("tweet"));
    }
}
