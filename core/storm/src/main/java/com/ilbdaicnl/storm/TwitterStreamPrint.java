package com.ilbdaicnl.storm;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Tuple;

import com.fasterxml.jackson.databind.node.ObjectNode;

import twitter4j.Status;

public class TwitterStreamPrint extends BaseBasicBolt {
	@Override
    public void execute(Tuple tuple, BasicOutputCollector collector) {
        System.out.println("\u001B[31m"+tuple.getValueByField("error")+"\u001B[0m");
       
//        BufferedWriter bw = null;
//
//        try {
//           bw = new BufferedWriter(new FileWriter("sample.txt", true));
//           bw.write(tuple.toString());
//           bw.newLine();
//           bw.flush();
//        } catch (IOException ioe) {
//        	ioe.printStackTrace();
//        } finally {                    
//        	if (bw != null) try {
//        		bw.close();
//        	} catch (IOException ioe2) {
//        		ioe2.printStackTrace();
//        	}
//        } 
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer ofd) {
    }
}
