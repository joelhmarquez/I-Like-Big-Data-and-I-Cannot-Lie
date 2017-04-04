import storm
import json
import math
# from cassandra.io.libevreactor import LibevConnection
# Previous not built for Windows
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

CREATE_COLUMNS = "id text PRIMARY KEY, tweettext text, lat text, lng text, time text, location text, score int, state text"

class insertTweetData(storm.BasicBolt):
    global CREATE_COLUMNS

    def process(self,tup):
        tweet = tup.values[0]
        self.text = tweet['tweettext']
        self.state = tweet['state']
        self.time = int(tweet['time'])
        self.time = int(math.floor(self.time//3600))
        # self.insert(tweet)
        storm.emit([self.insert(tweet)]) #We shouldn't have to emit at this point.  This should be the end of the storm path
    
    def insert(self,tweet):
        # Need to figure out authentication for connecting to server
        # authProvider = PlainTextAuthProvider(username='internal', password='fuckapplebees')
        # cluster = Cluster(["0.0.0.0"],port=9042)#,protocol_version=2,auth_provider=authProvider)
        # cluster.connection_class = LibevConnection
        # session = cluster.connect()
        # session.execute("CREATE KEYSPACE IF NOT EXISTS "+self.state+" WITH replication = {'class':'SimpleStrategy', 'replication_factor':3};")
        # selectDB = "USE "+self.state+";"
        insertData = "INSERT INTO \""+str(self.time)+"\" JSON '"+json.dumps(tweet)+"';"
        return insertData #This is for testing purposes
        # session.execute(selectDB)
        # session.set_keyspace(self.state)
        # try:
        #     #print(insertData)
        #     session.execute(insertData)

        # except Exception as e:
        #     createTable = "CREATE TABLE \""+str(self.time)+"\"("+CREATE_COLUMNS+");"
        #     print(createTable)
        #     try:
        #         session.execute(createTable)
        #         try:
        #             session.execute(insertData)
                   
        #         #except Exception as e:
        #             #print("Error inserting data after creating table")

        #     #except Exception as e:
        #         #print("Error creating table")

        # cluster.shutdown()


insertTweetData().run()
