import storm
import json
import math
# from cassandra.io.libevreactor import LibevConnection
# Previous not built for Windows
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

CREATE_COLUMNS = "id text PRIMARY KEY, tweettext text, lat text, lng text, time long, location text, sentimentscore double, state text"

class insertTweetData(storm.BasicBolt):
    global CREATE_COLUMNS

    def process(self,tup):
        tweet = tup.values[0]
        if tweet['id'] == None:
            tweet['id'] = ""
        self.id = tweet['id']

    	if tweet['tweettext'] == None:
    		tweet['tweettext'] = ""

        self.text = tweet['tweettext']
        self.text = self.text.replace("'","")
        self.text = self.text.replace("\"","")

        if tweet['lat'] == None:
            tweet['lat'] = ""
        self.lat = tweet['lat']

        if tweet['lng'] == None:
            tweet['lng'] = ""
        self.lng = tweet['lng']

        if tweet['location'] == None:
            tweet['location'] = ""
        self.location = tweet['location']

        if tweet['sentimentscore'] == None:
            tweet['sentimentscore'] = "0.0"
        self.score = float(tweet['sentimentscore'])

        if tweet['state'] == None:
            tweet['state'] = ""
        self.state = tweet['state']

        if tweet['time'] == None:
            tweet['time'] = "0"
        self.time = long(tweet['time'])
        #self.time = int(math.floor(self.time//3600000))
        self.insert(tweet)
    
    def insert(self,tweet):
        cluster = Cluster(['172.31.3.194'], port=9042)
        try:
            session = cluster.connect()
            selectDB = "USE twittertweets;"
            insertData = "INSERT INTO "+self.state+" (id, tweettext, lat, lng, time, location, sentimentscore, state) VALUES (\'"+self.id+"\',\'"+self.text+"\',\'"+self.lat+"\',\'"+self.lng+"\',"+str(self.time)+",\'"+self.location+"\',"+str(self.score)+",\'"+self.state+"\');"
            
            try:
                session.execute(selectDB)

                try:
                    session.execute(insertData)
                    success = "Successfully inserted"
                    storm.emit([success])
                
                except Exception as e:
                    createTable = "CREATE TABLE "+self.state+"("+CREATE_COLUMNS+");"

                    try:
                        session.execute(createTable)
                        try:
                            session.execute(insertData)
                            success = "Successfully inserted"
                            storm.emit([success])
                   
                        except Exception as e:
                            error = "Unable to insert data. Query: "+insertData+" error: "+str(e)
                            storm.emit([error])
                    except Exception as e:
                        error = "Unable to CREATE TABLE "+self.state+" error: "+str(e)
                        storm.emit([error])
            except Exception as e:
                error = "Unable to select keyspace twittertweets error: "+str(e)
                storm.emit([error])
        except Exception as e:
            error = "Unable to connect to Cassandra error: "+str(e)
            storm.emit([error])
        
        cluster.shutdown()


insertTweetData().run()

