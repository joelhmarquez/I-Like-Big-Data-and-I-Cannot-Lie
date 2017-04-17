#!/bin/bash

wget http://packages.elassandra.io/deb/elassandra_2.1.1-18.1.4_all.deb
dpgk -i elassandra_2.1.1-18.1.4_all.deb
sudo apt-get clean
sudo apt-get install elassandra
