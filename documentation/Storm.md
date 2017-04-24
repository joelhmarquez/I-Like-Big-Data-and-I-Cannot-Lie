Requirements (download the following)
Zookeeper
mkdir /tmp/zookeeper
Set datadir in conf/zoo.cfg to use newly made directory
sudo mv zookeeper /opt
Apache storm
mkdir /tmp/storm
Set datadir in conf/storm.yaml to use newly made directory
sudo mv apache-storm /opt
Leiningen (Needed for python storm implementation)
mkdir ~/bin
edit ~/.bashrc
Add ~/bin to path at end of file
export PATH=$PATH:~/bin
$bash <<< yes this is actually a command. It refreshes your shell to add the path in
cd ~/bin
wget <link for leininigen>
chmod 755 <file>
lein <<< seriously this isn’t a trick. Actually a command now
Sparse (Needed for python storm implementation)
pip install streamparse
At least 1 gb of available ram
Setting up environment
Start /opt/zookeeper (might have to do this as sudo)
./opt/zookeeper-3.4.9/bin/zkServer.sh start
Start Apache Storm (might need to do this as sudo as well)
cd /opt/apache-storm-1.0.3/bin
./storm nimbus &
[1] 5893
./storm supervisor &
[2] 5945
./storm ui &
[3] 5982
jobs 
Prints the job id’s from the previous commands
disown %1
disown %2
disown %3
This separates the jobs of id’s 1,2,3 from user and keep the process persistent after logout so it keeps running on the server

Creating a project
sparse quickstart wordcount
sparse run
Reference
https://vincenzogulisano.com/2015/07/30/5-minutes-storm-installation-guide-single-node-setup/
https://www.parsely.com/misc/slides/odsc-streams/#1
https://github.com/Parsely/streamparse
http://streamparse.readthedocs.io/en/stable/quickstart.html
https://www.parsely.com/misc/slides/logs/notes/#word-count-bolt-in-python
https://github.com/technomancy/leiningen#readme
