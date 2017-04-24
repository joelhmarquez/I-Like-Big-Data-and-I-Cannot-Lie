package com.ilbdaicnl.resources;

//import java.io.BufferedReader;
//import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Properties;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ResourceMgr {
	private static final ResourceMgr instance = new ResourceMgr();
	private String consumerKey;
	private String consumerSecret;
	private String accessToken;
	private String accessTokenSecret;
	List<String> keyWords = new ArrayList<String>();
	
	List<String> gmapsApiKeys;
	
	final Logger logger = LoggerFactory.getLogger(ResourceMgr.class);
	 
	protected ResourceMgr() {
        
        /* Reading in twitter oauth values, google maps api key and keyWords*/
        try {
        	Properties env = new Properties();
            InputStream stream = Thread.currentThread().getContextClassLoader().getResourceAsStream("config.properties");
			env.load(stream);
			this.consumerKey = env.getProperty("consumer.key");
			this.consumerSecret = env.getProperty("consumer.secret");
			this.accessToken = env.getProperty("access.token");
			this.accessTokenSecret = env.getProperty("access.token.secret");
			
			this.gmapsApiKeys = new ArrayList<String>(Arrays.asList(env.getProperty("google.keys").split("\\s*,\\s*")));
			
			logger.info("Successfully read in environment variables and keywords");
		} catch (IOException e) {
			logger.error("Error reading in environment variables or keywords: " + e.getMessage());
		} 
	}
 
	public static ResourceMgr getInstance() {
		return instance;
	}

	public String getConsumerKey() {
		return consumerKey;
	}

	public String getConsumerSecret() {
		return consumerSecret;
	}

	public String getAccessToken() {
		return accessToken;
	}

	public String getAccessTokenSecret() {
		return accessTokenSecret;
	}

	public List<String> getKeyWords() {
		return keyWords;
	}

	public String getApiKey() {
		return gmapsApiKeys.get(0);
	}
	
	public String refreshKey(){
		System.out.println("Reset Key");
		String currentKey = gmapsApiKeys.get(0);
		gmapsApiKeys.remove(0);
		gmapsApiKeys.add(currentKey);
		
		return gmapsApiKeys.get(0);
	}
}
