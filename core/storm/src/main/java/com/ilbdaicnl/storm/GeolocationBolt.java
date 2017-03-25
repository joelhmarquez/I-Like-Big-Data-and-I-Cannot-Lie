package com.ilbdaicnl.storm;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import com.fasterxml.jackson.databind.node.ObjectNode;
import com.google.maps.GeoApiContext;
import com.google.maps.GeocodingApi;
import com.google.maps.model.GeocodingResult;
import com.google.maps.model.LatLng;

public class GeolocationBolt extends BaseBasicBolt {
	public void execute(Tuple tuple, BasicOutputCollector collector) {
		ObjectNode tweet = (ObjectNode) tuple.getValueByField("tweet");
		
		GeoApiContext context = new GeoApiContext().setApiKey("");
		
		/* If lat and lng from status are present */
		if(!tweet.findValue("lat").asText().equals("null") && !tweet.findValue("lng").asText().equals("null")){
			LatLng location = new LatLng(tweet.findValue("lat").asDouble(), tweet.findValue("lng").asDouble());
			GeocodingResult[] results = null;
			try {
				results =  GeocodingApi.reverseGeocode(context, location).await();
				tweet.put("state", results[0].addressComponents[results[0].addressComponents.length - 2].longName);
				tweet.put("lat", results[0].geometry.location.lat);
				tweet.put("lat", results[0].geometry.location.lng);
			} catch (Exception e) {
				e.printStackTrace();
			}
		/* If lat and lng from status are not present but location is*/
		} else  if(tweet.findValue("lat").asText().equals("null") && !tweet.findValue("location").asText().equals("null")){
			GeocodingResult[] results = null;
			try {
				results =  GeocodingApi.geocode(context, tweet.findValue("location").asText()).await();
			} catch (Exception e) {
				e.printStackTrace();
			}
			try{
				tweet.put("lat", results[0].geometry.location.lat);
				tweet.put("lng", results[0].geometry.location.lng);
				tweet.put("state", results[0].addressComponents[results[0].addressComponents.length - 2].longName);
			} catch (ArrayIndexOutOfBoundsException ob) {
				tweet.put("state", "null");
			}
		} else {
			tweet.put("state", "null");
		}
		
		collector.emit(new Values(tweet));
	}
	 @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
    	declarer.declare(new Fields("tweet"));
    }
}
