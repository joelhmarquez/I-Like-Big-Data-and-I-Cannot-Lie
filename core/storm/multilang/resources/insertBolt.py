import storm
import json
import math
# from cassandra.io.libevreactor import LibevConnection
# Previous not built for Windows
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

CREATE_COLUMNS = "id text PRIMARY KEY, tweettext text, lat text, lng text, time text, location text, sentimentscore int, state text"

class insertTweetData(storm.BasicBolt):
    global CREATE_COLUMNS

    def process(self,tup):
        tweet = tup.values[0]
        self.text = tweet['tweettext']
        self.state = tweet['state']
        self.time = int(tweet['time'])
        self.time = int(math.floor(self.time//3600))
        self.insert(tweet)
    
    def insert(self,tweet):
        # Need to figure out how to emit an error properly for logging
        cluster = Cluster(["172.31.35.21"],port=9042)
        # cluster.connection_class = LibevConnection
        try:
            session = cluster.connect()
            selectDB = "USE "+self.state+";"
            insertData = "INSERT INTO \""+str(self.time)+"\" JSON '"+json.dumps(tweet)+"';"
            try:
                session.execute(selectDB)

                try:
                    session.execute(insertData)

                except Exception as e:
                    createTable = "CREATE TABLE \""+str(self.time)+"\"("+CREATE_COLUMNS+");"

                    try:
                        session.execute(createTable)
                        try:
                            session.execute(insertData)
                   
                        except Exception as e:
                            storm.emit([e])

                    except Exception as e:
                        storm.emit([e])
            except Exception as e:
                storm.emit([e])
        except Exception as e:
            storm.emit([e])
        cluster.shutdown()


insertTweetData().run()
