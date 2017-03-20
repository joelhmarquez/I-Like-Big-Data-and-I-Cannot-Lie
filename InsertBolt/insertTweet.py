import storm
import json
import math
# from cassandra.io.libevreactor import LibevConnection
# Previous not built for Windows
from cassandra.cluster import Cluster

CREATE_COLUMNS = "id text PRIMARY KEY, text text, lat text, lng text, time text, location text, score int, state text"

class insertTweetData(storm.BasicBolt):
    global CREATE_COLUMNS

    def initialize(self,tweet):
        self.state = tweet['state']
        self.time = int(tweet['time'])
        self.time = floor(self.time/3600)

    def insert(self,tweet):
        # Need IP address for Cassandra Server
        # Need to figure out authentication for connecting to server
        cluster = Cluster('192.168.1.1')
        # cluster.connection_class = LibevConnection
        session = cluster.connect()
        selectDB = "USE "+self.state+";"
        insertData = "INSERT INTO "+self.state+"."+self.time+" JSON "+json.dumps(tweet)+";"
        session.execute(selectDB)
        try:
            session.execute(insertData)
            break
        except Exception as e:
            print("Error inserting data {}, {}".format(e.errno, e.strerror))
            createTable = "CREATE TABLE "+self.time+"("+CREATE_COLUMNS+");"
            try:
                session.execute(createTable)
                break
                try:
                    session.execute(insertData)
                    break
                except Exception as e:
                    print("Error inserting data after creating table {} {}".format(e.errno, e.strerror))
                    break
            except Exception as e:
                print("Error creating table {} {}".format(e.errno, e.strerror))
                break

        cluster.shutdown()

            
insertTweetData().run()