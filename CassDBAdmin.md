#Cassandra Database Administration
+ Written by Micheal Swisher

## Preface 
+ Requirements:
 * Debian based host operating system (Ubuntu 14.04+, Debian 7+)
+ Openjdk 8
 * Installation instructions
 * Required packages: openjdk-8-jdk openjdk-8-jre openjdk-8-headless
### Installation
+ Follow Debian instructions to install from the command line http://cassandra.apache.org/download/
+ Do additional setup if needed by modifying values in /etc/cassandra/cassandra.yaml
 * http://cassandra.apache.org/doc/latest/getting_started/configuring.html has info about what is in the cassandra.yaml
 * Example of how to change cluster name here
## Interaction
+ Get sysinfo about db
 * user:~$ nodetool status
+ Interactive shell using CQL
 * user:~$ cqlsh
+ Useful commands
 * Describe, show, select * from <table>
## Java
+ Use DataStax Drivers
 * They exist on GitHub
## Miscellaneous
+ Key terms
 * Keyspace is analogous to SQL Database
 * Column Family (also table in Cassandra) is a table
 * Column is a dictionary
 * Super Column is like a complex dictionary
+ Setting up cluster from cqlsh
 * Create Keyspace
 * 1. CREATE KEYSPACE IF NOT EXISTS cycling WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 };
 * Switch to keyspace
 * 1. USE cycling;
 * Add table to keyspace
 * 1. INSERT INTO cycling.cyclist_category JSON '{  "category" : "GC",   "points" : 780,   "id" : "829aa84a-4bba-411f-a4fb-38167a987cda",  "lastname" : "SUTHERLAND" }';
 * Visualize keyspace and tables
 * 1. Describe keyspaces      <<< prints all keyspaces
 * 2. Describe cycling            <<< prints schema
 * 3. Dump tables: Select * from <table name>
+ Securing Cassandra
 * Add replication for single node
 * 1. ALTER KEYSPACE "system_auth" WITH REPLICATION =  { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
 * Change cassandra.yaml authenticator to PasswordAuthenticator, authorizer to CassandraAuthorizer
 * Restart cassandra service
 * Use “nodetool repair”
 * Login using “cqlsh -u cassandra -p cassandra”
 * Create new admin
 ** CREATE ROLE <new_super_user> WITH PASSWORD = '<some_secure_password>' AND SUPERUSER = true AND LOGIN = true;
 * Logout then log back in with new admin
 * Disable old cassandra admin
 * 1. ALTER ROLE cassandra WITH PASSWORD='SomeNonsenseThatNoOneWillThinkOf' AND SUPERUSER=false;
## References
+ https://www.tutorialspoint.com/cassandra/cassandra_create_keyspace.htm
+ https://blog.evanweaver.com/2009/07/06/up-and-running-with-cassandra/
+ http://schabby.de/cassandra-getting-started/
+ https://academy.datastax.com/resources/getting-started-apache-cassandra-and-java-part-i?unit=getting-started-apache-cassandra-and-java-part-i
+ https://docs.datastax.com/en/cassandra/3.0/cassandra/configuration/secureConfigNativeAuth.html
+ http://docs.datastax.com/en/cassandra/2.1/cassandra/security/secure_config_native_authorize_t.html
+ http://docs.datastax.com/en/cql/3.1/cql/cql_using/update_ks_rf_t.html
+ https://docs.datastax.com/en/cassandra/3.0/cassandra/configuration/secureConfigNativeAuth.html



