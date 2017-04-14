import storm
import json
import math
import re
# from cassandra.io.libevreactor import LibevConnection
# Previous not built for Windows
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

CREATE_COLUMNS = "id text PRIMARY KEY, tweettext text, lat text, lng text, time text, location text, sentimentscore text, state text"

class insertTweetData(storm.BasicBolt):
    global CREATE_COLUMNS

    def process(self,tup):
        tweet = tup.values[0]
        #tweet['tweet'] = tweet['tweet'].replace("'","")
        #tweet['tweet'] = tweet['tweet'].replace("\"","")
        #tweet['tweet'] = tweet['tweet'].replace("\/","")
        self.id = tweet['id']
        self.text = tweet['tweettext']
        self.text = self.text.replace("'","")
        self.text = self.text.replace("\"","")
        #self.text = self.text.replace("\\"," ")
        #self.text = self.text.replace("@","AT:")
        #self.text = re.sub(r'^https?:\/\/.*[\r\n]*', '', self.text, flags=re.MULTILINE)
        self.lat = tweet['lat']
        self.lng = tweet['lng']
        self.location = tweet['location']
        self.score = tweet['sentimentscore']
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
            #insertData = "INSERT INTO \""+str(self.time)+"\" JSON '"+json.dumps(tweet)+"';"
            insertData = "INSERT INTO \""+str(self.time)+"\" (id, tweettext, lat, lng, time, location, sentimentscore, state) VALUES (\'"+self.id+"\',\'"+self.text+"\',\'"+self.lat+"\',\'"+self.lng+"\',\'"+tweet['time']+"\',\'"+self.location+"\',\'"+self.score+"\',\'"+self.state+"\');"
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
                            error = "Unable to insert data. Query: "+insertData
                            storm.emit([error])

                    except Exception as e:
                        error = "Unable to CREATE TABLE "+str(self.time)
                        storm.emit([error])
            except Exception as e:
                error = "Unable to select keyspace "+self.state
                storm.emit([error])
        except Exception as e:
            storm.emit(["Unable to connect to Cassandra"])
        cluster.shutdown()


insertTweetData().run()

