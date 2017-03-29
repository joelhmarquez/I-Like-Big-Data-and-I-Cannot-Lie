package com.ilbdaicnl.resources;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import twitter4j.Status;

public class TweetObject {
	private String id;
	private String text;
	private String lat;
	private String lng;
	private String time;
	private String location;
	private String state;
	private String sentimentScore;
	
	public TweetObject(Status tweet){
		this.id = Long.toString(tweet.getId());
		this.text = tweet.getText();
		this.lat = tweet.getGeoLocation()!=null ? Double.toString(tweet.getGeoLocation().getLatitude()) : null;
		this.lng = tweet.getGeoLocation()!=null ? Double.toString(tweet.getGeoLocation().getLongitude()) : null;
		this.time = Long.toString(tweet.getCreatedAt().getTime());
		this.location = tweet.getUser()!=null ? tweet.getUser().getLocation(): null;
		this.state = null;
		this.sentimentScore = null;
	}
	
	public TweetObject(ObjectNode tweet){
		this.id = tweet.findValue("id").asText();
		this.text = tweet.findValue("text").asText();
		this.lat = tweet.findValue("lat").asText();
		this.lng = tweet.findValue("lng").asText();
		this.time = tweet.findValue("time").asText();
		this.location = tweet.findValue("location").asText();
		this.state = tweet.findValue("state").asText();
		this.sentimentScore = tweet.findValue("sentimentScore").asText();
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
	public String getSentimentScore() {
		return sentimentScore;
	}

	public void setSentimentScore(String sentimentScore) {
		this.sentimentScore = sentimentScore;
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
		formattedTweet.put("sentimentScore", this.sentimentScore);
		
		return formattedTweet;
	}
}
