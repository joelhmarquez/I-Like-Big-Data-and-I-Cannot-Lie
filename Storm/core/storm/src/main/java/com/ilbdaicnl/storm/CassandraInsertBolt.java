package com.ilbdaicnl.storm;

import java.util.Map;

import org.apache.storm.task.ShellBolt;
import org.apache.storm.topology.IRichBolt;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;

public class CassandraInsertBolt extends ShellBolt implements IRichBolt{
		public CassandraInsertBolt() {
	      super("python", "resources/insertBolt.py");
	    }

	    @Override
	    public void declareOutputFields(OutputFieldsDeclarer declarer) {
	      
	    }

	    @Override
	    public Map<String, Object> getComponentConfiguration() {
	      return null;
	    }
}
