package com.ilbdaicnl.storm;


import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Tuple;

public class TwitterStreamPrint extends BaseBasicBolt {
	@Override
    public void execute(Tuple tuple, BasicOutputCollector collector) {
        System.out.println("\u001B[33m"+tuple.getValueByField("error")+"\u001B[0m");
//		System.out.println(tuple);
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer ofd) {
    }
}
