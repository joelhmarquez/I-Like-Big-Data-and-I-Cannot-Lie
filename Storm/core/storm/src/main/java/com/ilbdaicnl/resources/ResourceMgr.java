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
	private String gnipUsername;
	private String gnipPassword;
	private String gnipUrl;
	
	final Logger logger = LoggerFactory.getLogger(ResourceMgr.class);
	 
	protected ResourceMgr() {
        
        /* Reading in twitter oauth values, google maps api key and keyWords*/
        try {
        	Properties env = new Properties();
            InputStream stream = Thread.currentThread().getContextClassLoader().getResourceAsStream("config.properties");
			env.load(stream);
			this.gnipUsername = env.getProperty("gnip.username");
			this.gnipPassword = env.getProperty("gnip.password");
			this.gnipUrl = env.getProperty("gnip.url");
					
			logger.info("Successfully read in environment variables");
		} catch (IOException e) {
			logger.error("Error reading in environment variables: " + e.getMessage());
		} 
	}
 
	public static ResourceMgr getInstance() {
		return instance;
	}

	public String getGnipUsername() {
		return gnipUsername;
	}
	
	public String getGnipPassword() {
		return gnipPassword;
	}
	public String getGnipUrl() {
		return gnipUrl;
	}
}
