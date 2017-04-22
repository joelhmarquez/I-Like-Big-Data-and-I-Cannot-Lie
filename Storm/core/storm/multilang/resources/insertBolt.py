import storm
import json
import math
# from cassandra.io.libevreactor import LibevConnection
# Previous not built for Windows
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

CREATE_COLUMNS = "id text PRIMARY KEY, tweettext text, lat text, lng text, time text, location text, sentimentscore text, state text"

class insertTweetData(storm.BasicBolt):
    global CREATE_COLUMNS

    def process(self,tup):
        tweet = tup.values[0]

        self.id = tweet['id']
        self.text = tweet['tweettext']
        self.text = self.text.replace("'","")
        self.text = self.text.replace("\"","")
        self.lat = tweet['lat']
        self.lng = tweet['lng']
        self.location = tweet['location']
        self.score = tweet['sentimentscore']
        self.state = tweet['state']
        self.time = int(tweet['time'])
        self.time = int(math.floor(self.time//3600000))
        self.insert(tweet)
    
    def insert(self,tweet):
        # Need to figure out how to emit an error properly for logging
        cluster = Cluster(["172.31.3.194"],port=9042)

        try:
            session = cluster.connect()
            selectDB = "USE "+self.state+";"
            insertData = "INSERT INTO \""+str(self.time)+"\" (id, tweettext, lat, lng, time, location, sentimentscore, state) VALUES (\'"+self.id+"\',\'"+self.text+"\',\'"+self.lat+"\',\'"+self.lng+"\',\'"+tweet['time']+"\',\'"+self.location+"\',\'"+self.score+"\',\'"+self.state+"\');"
            
            try:
                session.execute(selectDB)

                try:
                    session.execute(insertData)
                    success = "Successfully inserted"
                    storm.emit([sucess])
                
                except Exception as e:
                    createTable = "CREATE TABLE \""+str(self.time)+"\"("+CREATE_COLUMNS+");"

                    try:
                        session.execute(createTable)
                        try:
                            session.execute(insertData)
                            success = "Successfully inserted"
                            storm.emit([sucess])
                   
                        except Exception as e:
                            error = "Unable to insert data. Query: "+insertData
                            storm.emit([str(e)])
                    except Exception as e:
                        error = "Unable to CREATE TABLE "+str(self.time)
                        storm.emit([str(e)])
            except Exception as e:
                error = "Unable to select keyspace "+self.state
                storm.emit([str(e)])
        except Exception as e:
            error = "Unable to connect to Cassandra with Tweet object: \'"+self.id+"\',\'"+self.text+"\',\'"+self.lat+"\',\'"+self.lng+"\',\'"+tweet['time']+"\',\'"+self.location+"\',\'"+self.score+"\',\'"+self.state+"\'"
            storm.emit([str(e)])
        
        cluster.shutdown()


insertTweetData().run()

