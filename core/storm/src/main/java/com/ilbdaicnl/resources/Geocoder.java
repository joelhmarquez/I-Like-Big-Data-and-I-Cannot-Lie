package com.ilbdaicnl.resources;

import com.google.maps.GeoApiContext;
import com.google.maps.GeocodingApi;
import com.google.maps.model.AddressComponent;
import com.google.maps.model.GeocodingResult;
import com.google.maps.model.LatLng;

public class Geocoder {
	
	public TweetObject setState(TweetObject tweet){
		/* Reading in google maps api key values */
		ResourceMgr resourceMgr = ResourceMgr.getInstance();
		String apiKey = resourceMgr.getApiKey();
	    
		GeoApiContext context = new GeoApiContext().setApiKey(apiKey);
		
		GeocodingResult[] results = null;

		/* If lat and lng from status are present */
		if(tweet.getLat() != null && tweet.getLng() != null){
			LatLng location = new LatLng(Double.valueOf(tweet.getLat()), Double.valueOf(tweet.getLng()));
			try{
				results =  GeocodingApi.reverseGeocode(context, location).await();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		/* If lat/lng are null but a user profile location is set */
		else if(tweet.getLocation() != null){
			try{
				results =  GeocodingApi.geocode(context, tweet.getLocation()).await();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		try{
			tweet.setLat(Double.toString(results[0].geometry.location.lat));
			tweet.setLng(Double.toString(results[0].geometry.location.lng));
			tweet.setState(getState(results[0].addressComponents));
		} catch (ArrayIndexOutOfBoundsException | NullPointerException e) {
			tweet.setState(null);
		}
		
		return tweet;
	}
	
	private String getState(AddressComponent[] addressComponents){
		for(int i=0; i<addressComponents.length; i++){
			if(addressComponents[i].types[0].toString().equals("administrative_area_level_1")){
				return addressComponents[i].longName.replaceAll("\\s","");
			}
		}
		return null;
	}
}
