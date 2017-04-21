package com.ilbdaicnl.resources;

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
	
	public TweetObject(JsonNode tweet){
		this.id = tweet.findValuesAsText("id").isEmpty() ? null : tweet.findValuesAsText("id").get(0);
		this.text = tweet.findValuesAsText("body").isEmpty() ? null : tweet.findValuesAsText("body").get(0);
		this.lat = null;
		this.lng = null;
		this.time = tweet.findValuesAsText("timePosted").isEmpty() ? null : tweet.findValuesAsText("timePosted").get(0);
		this.location = tweet.findValuesAsText("location").isEmpty() ? null : tweet.findValuesAsText("location").get(0);
		this.state = tweet.findValuesAsText("region").isEmpty() ? null : tweet.findValuesAsText("region").get(0).replaceAll("\\s+","");
		this.sentimentscore = "null";
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
