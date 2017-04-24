package com.ilbdaicnl.storm;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Tuple;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.fasterxml.jackson.databind.node.ObjectNode;


public class LoggerBolt extends BaseBasicBolt {
	public void execute(Tuple tuple, BasicOutputCollector collector) {
		ObjectNode error = (ObjectNode) tuple.getValueByField("error");
		final Logger logger = LoggerFactory.getLogger(TwitterStreamTopology.class);
		
		logger.error(error.get("error").asText());
	}
	 @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
    	
    }
}
