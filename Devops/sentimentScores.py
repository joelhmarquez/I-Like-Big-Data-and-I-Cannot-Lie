from cassandra.cluster import Cluster
import sys
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

session.execute("USE twittertweets;")
count = 0
for item in statesToInsert:
#Insert Tables
        neutral = session.execute("select count(*) from "+item+" where sentimentscore=0 allow filtering;")[0]
        neutral = str(neutral).split('=')
        neutral = neutral[1]
        neutral = neutral.replace(")","")
        #print(item+" sentiment=0 count="+StateCount)
        hate = session.execute("select count(*) from "+item+" where sentimentscore>0 allow filtering;")[0]
        hate = str(hate).split('=')
        hate = hate[1]
        hate = hate.replace(")","")
        total = int(neutral) + int(hate)
        print(item+" Hate Percentage: {}% Total: {}".format(float((float(hate)/float(total))*100),total))

cluster.shutdown()