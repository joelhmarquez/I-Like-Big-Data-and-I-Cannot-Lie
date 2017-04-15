package com.ilbdaicnl.storm;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import com.ilbdaicnl.resources.Geocoder;
import com.ilbdaicnl.resources.TweetObject;

public class GeolocationBolt extends BaseBasicBolt {
	public void execute(Tuple tuple, BasicOutputCollector collector) {
		TweetObject tweet = (TweetObject) tuple.getValueByField("tweet");
		
		Geocoder geocoder = new Geocoder();
		
		TweetObject stateSet = geocoder.setState(tweet);
		
		if(stateSet.getState() != null) collector.emit("success", new Values(geocoder.setState(tweet).asJSON()));
		collector.emit(new Values(geocoder.setState(tweet).asJSON()));
	}
	 @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
    	declarer.declareStream("success", new Fields("tweet"));
    }
}
