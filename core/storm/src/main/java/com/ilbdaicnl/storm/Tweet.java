package com.ilbdaicnl.storm;

public class Tweet {
	private String text;
	private String retweetCount;
	private String lat;
	private String lng;
	private String time;
	private String location;
	
	public String getText() {
		return text;
	}
	public void setText(String text) {
		this.text = text;
	}
	public String getRetweetCount() {
		return retweetCount;
	}
	public void setRetweetCount(String retweetCount) {
		this.retweetCount = retweetCount;
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
}
