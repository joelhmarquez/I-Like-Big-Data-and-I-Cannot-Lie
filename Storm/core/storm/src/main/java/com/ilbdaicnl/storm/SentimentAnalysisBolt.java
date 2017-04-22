package com.ilbdaicnl.storm;

import java.util.Map;

import org.apache.storm.task.ShellBolt;
import org.apache.storm.topology.IRichBolt;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;

public class SentimentAnalysisBolt extends ShellBolt implements IRichBolt{
		public SentimentAnalysisBolt() {
	      super("python", "resources/sentiment.py");
	    }

	    @Override
	    public void declareOutputFields(OutputFieldsDeclarer declarer) {
	      declarer.declare(new Fields("tweet"));
	    }

	    @Override
	    public Map<String, Object> getComponentConfiguration() {
	      return null;
	    }
}
