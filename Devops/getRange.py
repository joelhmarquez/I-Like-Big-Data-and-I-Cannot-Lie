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
dates = open("dates.txt", "r")
events = open("events.txt", "r")
session.execute("USE twittertweets;")
events = events.split(" ")
count = 0
for line in dates:
        print(events[count])
        print("=========================")
        line = line.split(" ")
        for item in statesToInsert:
                StateCount = session.execute("select count(*) from "+item+" where time>="+line[0]+" and time<="+line[1]+" and sentimentscore=0 allow filtering;")[0]
                StateCount = str(StateCount).split('=')
                StateCount = StateCount[1]
                StateCount = StateCount.replace(")","")
                print(item+" sentiment EQUALS 0 count="+StateCount)
                StateCount = session.execute("select count(*) from "+item+" where time>="+line[0]+" and time<="+line[1]+" and sentimentscore>0 allow filtering;")[0]
                StateCount = str(StateCount).split('=')
                StateCount = StateCount[1]
                StateCount = StateCount.replace(")","")
                print(item+" sentiment NOT EQUAL 0 count="+StateCount)
        count += 1
dates.close()
dates = open("dates2.txt", "r")
print(events[count])
print("=========================")
for line in dates:
        line = line.split(" ")
        for item in statesToInsert:
                StateCount = session.execute("select count(*) from "+item+" where time>="+line[0]+" and time<="+line[1]+" and sentimentscore=0 allow filtering;")[0]
                StateCount = str(StateCount).split('=')
                StateCount = StateCount[1]
                StateCount = StateCount.replace(")","")
                print(item+" sentiment EQUALS 0 count="+StateCount)
                StateCount = session.execute("select count(*) from "+item+" where time>="+line[0]+" and time<="+line[1]+" and sentimentscore>0 allow filtering;")[0]
                StateCount = str(StateCount).split('=')
                StateCount = StateCount[1]
                StateCount = StateCount.replace(")","")
                print(item+" sentiment NOT EQUAL 0 count="+StateCount)

cluster.shutdown()