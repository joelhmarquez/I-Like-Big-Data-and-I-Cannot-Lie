package com.ilbdaicnl.resources;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.TimeZone;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;


public class TweetObject {
	private String id;
	private String text;
	private String lat;
	private String lng;
	private String time;
	private String location;
	private String state;
	private String sentimentscore;
	private String epoch;
	private String actualID;
	
	public TweetObject(JsonNode tweet) throws ParseException{
		List<String> ids = tweet.findValuesAsText("id");
		List<String> texts = tweet.findValuesAsText("body");
		List<String> times = tweet.findValuesAsText("postedTime");
		List<String> locations = tweet.findValuesAsText("location");
		List<String> states = tweet.findValuesAsText("region");
		
		if(!times.isEmpty()){
			String dateUTC = times.get(0);
			SimpleDateFormat df = new SimpleDateFormat(
				    "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'", Locale.US);
				df.setTimeZone(TimeZone.getTimeZone("UTC"));
		    Date date = df.parse(dateUTC);
		    epoch = Long.toString(date.getTime());
		}
		
		if(!ids.isEmpty()){
			String[] idList = ids.get(0).split(":");
			actualID = idList[2];
		}
		
		this.id = ids.isEmpty() ? null : actualID;
		this.text = texts.isEmpty() ? null : texts.get(0);
		this.lat = null;
		this.lng = null;
		this.time = times.isEmpty() ? null : epoch;
		this.location = locations.isEmpty() ? null : locations.get(0);
		this.state = states.isEmpty() ? null : states.get(0).replaceAll("\\s+","");
		this.sentimentscore = null;
	}
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getText() {
		return text;
	}
	public void setText(String text) {
		this.text = text;
	}
	public String getLat() {
		return lat;
	}
	public void setLat(String lat) {
		this.lat = lat;
	}
	public String getLng() {
		return lng;
	}
	public void setLng(String lng) {
		this.lng = lng;
	}
	public String getTime() {
		return time;
	}
	public void setTime(String time) {
		this.time = time;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public String getState() {
		return state;
	}
	public void setState(String state) {
		this.state = state;
	}
	public String getSentimentscore() {
		return sentimentscore;
	}

	public void setSentimentScore(String sentimentScore) {
		this.sentimentscore = sentimentScore;
	}
	
	public ObjectNode asJSON(){
		ObjectMapper mapper = new ObjectMapper();
		
		ObjectNode formattedTweet = mapper.createObjectNode();
		formattedTweet.put("id", this.id);
		formattedTweet.put("text", this.text);
		formattedTweet.put("lat", this.lat);
		formattedTweet.put("lng", this.lng);
		formattedTweet.put("time", this.time);
		formattedTweet.put("location", this.location);
		formattedTweet.put("state", this.state);
		formattedTweet.put("sentimentScore", this.sentimentscore);
		
		return formattedTweet;
	}
}
