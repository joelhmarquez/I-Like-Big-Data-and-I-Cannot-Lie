#Downloading and Installing Cassandra using Linux:

Document to provide helpful hints, links, structure of Cassandra

## Helpful Sites for resource information
+ Basic Info:
 * http://cassandra.apache.org/doc/latest/getting_started/index.html 
 * https://www.tutorialspoint.com/cassandra/cassandra_installation.htm
+ Installing: 
 * https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-04
+ For GUI implementation: A resource: 
 * https://github.com/sebgiroux/Cassandra-Cluster-Admin 
+ Setting up the client driver from a simple connect and query program: 
 * http://docs.datastax.com/en/developer/java-driver/3.1/manual/
+ Datastax Java Driver for Apache Cassandra
 * https://github.com/datastax/java-driver
 
## Download/Install:
+ Install Java or $java –version
+ echo "deb http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
+ echo "deb-src http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
+ In order to avoid package signature warnings during package updates 
 * gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
 * gpg --export --armor F758CE318D77295D | sudo apt-key add –
 * gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
 * gpg --export --armor 2B5C1B00 | sudo apt-key add –
 * gpg --keyserver pgp.mit.edu --recv-keys 0353B12C
 * gpg --export --armor 0353B12C | sudo apt-key add –
+ Update the database package and complete installation
 * sudo apt-get update
 * sudo apt-get install Cassandra
+ Checking if it worked
 * sudo service cassandra status
 * sudo nodetool status

## Running Cassandra (cqlsh) :
+ https://gist.github.com/Micka33/89897e1490240a56c036
+ cqlsh is a command line shell for interacting with Cassandra through CQL. It is shipped with every Cassandra package, and can be found in the bin/ directory alongside the cassandra executable. It connects to the single node specified on the command line.

## Record of useful commands
+ For checking status 
 * sudo service cassandra status
+ Running Cassandra
 * sudo service cassandra start
+ Stopping Cassandra
 * sudo service cassandra stop
+ Find Cassandra port
 * ps axu | grep Cassandra
 * sudo netstat -tulpn | grep -i listen | grep <pid>
 * or cqlsh> show host
+ Find cassandra version: 
 * select release_version from system.local;
 * or cqlsh> show version
+ For connecting to a single node
 * cqlsh> sudo nodetool status
 * cqlsh> SELECT cluster_name, listen_address FROM system.local;


