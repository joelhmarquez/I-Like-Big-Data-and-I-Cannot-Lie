package com.ilbdaicnl.storm;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Tuple;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class LoggerBolt extends BaseBasicBolt {
	public void execute(Tuple tuple, BasicOutputCollector collector) {
		String error = (String) tuple.getValueByField("error");
		final Logger logger = LoggerFactory.getLogger(TwitterStreamTopology.class);
		
		logger.error(error);
	}
	 @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
    	
    }
}
