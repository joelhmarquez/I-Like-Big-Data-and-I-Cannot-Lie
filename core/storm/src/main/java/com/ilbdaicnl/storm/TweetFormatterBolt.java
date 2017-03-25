package com.ilbdaicnl.storm;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import twitter4j.Status;


public class TweetFormatterBolt extends BaseBasicBolt {
	@Override
    public void execute(Tuple tuple, BasicOutputCollector collector) {
		Status tweet = (Status) tuple.getValueByField("tweet");
		
		String id = Long.toString(tweet.getId());
		String text = tweet.getText();
		String retweetCount = Integer.toString(tweet.getRetweetCount());
		String lat = tweet.getGeoLocation()!=null ? Double.toString(tweet.getGeoLocation().getLatitude()) : "null";
		String lng = tweet.getGeoLocation()!=null ? Double.toString(tweet.getGeoLocation().getLongitude()) : "null";
		String time = Long.toString(tweet.getCreatedAt().getTime());
		String location = tweet.getUser()!=null ? tweet.getUser().getLocation(): "null";
		
		ObjectMapper mapper = new ObjectMapper();
		
		ObjectNode formattedTweet = mapper.createObjectNode();
		formattedTweet.put("id", id);
		formattedTweet.put("text", text);
		formattedTweet.put("retweetCount", retweetCount);
		formattedTweet.put("lat", lat);
		formattedTweet.put("lng", lng);
		formattedTweet.put("time", time);
		formattedTweet.put("location", location);
		
		collector.emit(new Values(formattedTweet));
	}
	
    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
    	declarer.declare(new Fields("tweet"));
    }
}
