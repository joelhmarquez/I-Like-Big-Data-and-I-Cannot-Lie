#import storm
import json
import math
# from cassandra.io.libevreactor import LibevConnection
# Previous not built for Windows
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

CREATE_COLUMNS = "id text PRIMARY KEY, tweettext text, lat text, lng text, time text, location text, score int, state text"

class insertTweetData():#storm.BasicBolt):
    global CREATE_COLUMNS

    def __init__(self,tweet):
        self.text = tweet['tweettext']
        self.state = tweet['state']
        self.time = int(tweet['time'])
        self.time = int(math.floor(self.time//3600))

    def insert(self,tweet):
        # Need to figure out authentication for connecting to server
        # authProvider = PlainTextAuthProvider(username='internal', password='fuckapplebees')
        cluster = Cluster(["0.0.0.0"],port=9042)#,protocol_version=2,auth_provider=authProvider)
        # cluster.connection_class = LibevConnection
        session = cluster.connect()
        session.execute("CREATE KEYSPACE IF NOT EXISTS "+self.state+" WITH replication = {'class':'SimpleStrategy', 'replication_factor':3};")
        selectDB = "USE "+self.state+";"
        insertData = "INSERT INTO \""+str(self.time)+"\" JSON '"+json.dumps(tweet)+"';"
        session.execute(selectDB)
        session.set_keyspace(self.state)
        try:
            print(insertData)
            session.execute(insertData)

        except Exception as e:
            print("Error inserting data")
            createTable = "CREATE TABLE \""+str(self.time)+"\"("+CREATE_COLUMNS+");"
            print(createTable)
            try:
                session.execute(createTable)
                try:
                    print(insertData)
                    session.execute(insertData)
                   
                except Exception as e:
                    print("Error inserting data after creating table")

            except Exception as e:
                print("Error creating table")

        cluster.shutdown()


#insertTweetData().run()

# def main():
#     tweet = json.load(open("sampleTweets1.txt","r"))
#     tweet[0]['tweettext'] = tweet[0]['text']
#    # tweet[0]['retweetcount'] = tweet[0]['retweetCount']
#    # del tweet[0]['retweetCount']
#     del tweet[0]['text']
#     tweet = tweet[0]
#     testing = insertTweetData(tweet)