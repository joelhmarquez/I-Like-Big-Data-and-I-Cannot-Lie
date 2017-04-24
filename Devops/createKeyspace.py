from cassandra.cluster import Cluster
cluster = Cluster(['172.31.3.194'], port=9042)
session = cluster.connect()
statesToInsert = {
'Arkansas',
'Alabama',
'Arizona',
'Alaska',
'California',
'Colorado',
'Connecticut',
'Delaware',
'Florida',
'Georgia',
'Hawaii',
'Iowa',
'Idaho',
'Illinois',
'Indiana',
'Kansas',
'Kentucky',
'Louisiana',
'Massachusetts',
'Maryland',
'Maine',
'Michigan',
'Minnesota',
'Missouri',
'Mississippi',
'Montana',
'NorthCarolina',
'NorthDakota',
'Nebraska',
'NewHampshire',
'NewJersey',
'NewMexico',
'Nevada',
'NewYork',
'Ohio',
'Oklahoma',
'Oregon',
'Pennsylvania',
'RhodeIsland',
'SouthCarolina',
'SouthDakota',
'Tennessee',
'Texas',
'Utah',
'Virginia',
'Vermont',
'Washington',
'Wisconsin',
'WestVirginia',
'Wyoming'
}
session.execute("CREATE KEYSPACE twittertweets WITH REPLICATION={'class':'SimpleStrategy','replication_factor':3};")
session.execute("USE twittertweets;")
for item in statesToInsert:
#Insert Tables
        session.execute("CREATE TABLE " + item +"(id text PRIMARY KEY, tweettext text, lat text, lng text, time bigint, location text, sentimentscore double, state text);")
        session.execute("CREATE INDEX "+item+"TweetIndex on twittertweets."+item+"(tweettext);")
        session.execute("CREATE INDEX "+item+"ScoreIndex on twittertweets."+item+"(sentimentscore);")
        session.execute("CREATE INDEX "+item+"TimeIndex on twittertweets."+item+"(time);")
cluster.shutdown()