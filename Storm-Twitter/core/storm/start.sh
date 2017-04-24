#!/bin/bash

#Packaging Jars
mvn clean install

#Running Topology on Storm locally
storm jar target/storm-0.0.1-SNAPSHOT-jar-with-dependencies.jar com.ilbdaicnl.storm.TwitterStreamTopology
