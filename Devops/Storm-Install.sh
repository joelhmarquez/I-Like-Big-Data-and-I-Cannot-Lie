#!/bin/bash

# Install dependencies
sudo add-apt-repository ppa:openjdk-r/ppa -y
sudo apt-get update -y
sudo apt-get install openjdk-8-jdk openjdk-8-jre python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev -y

pip install --upgrade pip

sudo -H pip install streamparse

# Get source files for services
wget http://apache.mirrors.pair.com/zookeeper/stable/zookeeper-3.4.10.tar.gz
wget http://download.nextag.com/apache/storm/apache-storm-1.0.2/apache-storm-1.0.2.tar.gz


# Extract source files
sudo tar xvf zookeeper-3.4.10.tar.gz
sudo mv zookeeper-3.4.10 /opt/zookeeper

sudo mkdir /opt/zookeeper/datadir

sudo tar xvf apache-storm-1.0.2.tar.gz
sudo mv apache-storm-1.0.2 /opt/storm

sudo mkdir /opt/storm/datadir

# Setup for lein
mkdir ~/bin
echo 'export PATH=$PATH:~/bin' >> ~/.bashrc

$bash

cd ~/bin
wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
chmod 755 lein

cd ~/

# Add the configuration files for storm and zookeeper
wget 52.14.155.145/storm.yaml
mv storm.yaml /opt/storm/conf/

wget 52.14.155.145/zoo.cfg
mv zoo.cfg /opt/zookeeper/conf/

# Add symlink for streamparse
sudo ln -s /opt/storm/bin/storm /bin/storm

# Change owner of services to ubuntu
sudo chown -R ubuntu:ubuntu /opt/*

# Get script to update boot settings on system.
wget 52.14.155.145/rc.local
sudo cat rc.local > /etc/rc.local

# Restart system to initialize services
sudo reboot