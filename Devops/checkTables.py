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

session.execute("USE twittertweets;")
count = 0
for item in statesToInsert:
#Insert Tables
        StateCount = session.execute("select count(*) from "+item+";")[0]
        StateCount = str(StateCount).split('=')
        StateCount = StateCount[1]
        StateCount = StateCount.replace(")","")
        print(item+" count="+StateCount)
        count += int(StateCount)
print("Total Count: "+str(count))
cluster.shutdown()