#Storm

Document to outline how to implement and use Storm

## Requirements (download the following):
 
+ Zookeeper
  * mkdir /tmp/zookeeper
  1. Set datadir in conf/zoo.cfg to use newly made directory
  * sudo mv zookeeper /opt
+ Apache storm  
  * mkdir /tmp/storm
  * Set datadir in conf/storm.yaml to use newly made directory
  * sudo mv apache-storm /opt
+ Leiningen (Needed for python storm implementation)
  * mkdir ~/bin
  * edit ~/.bashrc
  1. Add ~/bin to path at end of file
  2. export PATH=$PATH:~/bin
  * $bash <<< yes this is actually a command. It refreshes your shell to add the path in
  * $ cd ~/bin
  * $ wget linkForLeininigen
  * $ chmod 755 fileName
  * $ lein 
+ Sparse (Needed for python storm implementation)
  * pip install streamparse
  * Note: At least 1 gb of available ram
+ Setting up environment
  * Start /opt/zookeeper (might have to do this as sudo)
  1. ./opt/zookeeper-3.4.9/bin/zkServer.sh start
  * Start Apache Storm (might need to do this as sudo as well)
  1. cd /opt/apache-storm-1.0.3/bin
  * ./storm nimbus &
  1. [1] 5893
  * ./storm supervisor &
  1. [2] 5945
  * ./storm ui &
  1. [3] 5982
  * jobs 
  1. Prints the job id’s from the previous commands
  * disown %1, disown %2, disown %3
  1. This separates the jobs of id’s 1,2,3 from user and keep the process persistent after logout so it keeps running on the server

+ Creating a project
  * sparse quickstart wordcount
  * sparse run
  
## Reference
+ https://vincenzogulisano.com/2015/07/30/5-minutes-storm-installation-guide-single-node-setup/
+ https://www.parsely.com/misc/slides/odsc-streams/#1
+ https://github.com/Parsely/streamparse
+ http://streamparse.readthedocs.io/en/stable/quickstart.html
+ https://www.parsely.com/misc/slides/logs/notes/#word-count-bolt-in-python
+ https://github.com/technomancy/leiningen#readme
