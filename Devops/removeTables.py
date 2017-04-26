from cassandra.cluster import Cluster
cluster = Cluster(['172.31.3.194'], port=9042)
session = cluster.connect()
tables = open("tables.txt", "r")
statesToInsert = {
'arkansas',
'alabama',
'arizona',
'alaska',
'california',
'colorado',
'connecticut',
'delaware',
'florida',
'georgia',
'hawaii',
'iowa',
'idaho',
'illinois',
'indiana',
'kansas',
'kentucky',
'louisiana',
'massachusetts',
'maryland',
'maine',
'michigan',
'minnesota',
'missouri',
'mississippi',
'montana',
'northcarolina',
'northdakota',
'nebraska',
'newhampshire',
'newjersey',
'newmexico',
'nevada',
'newyork',
'ohio',
'oklahoma',
'oregon',
'pennsylvania',
'rhodeIsland',
'southcarolina',
'southdakota',
'tennessee',
'texas',
'utah',
'virginia',
'vermont',
'washington',
'wisconsin',
'westvirginia',
'wyoming'
}
count = 0
for item in tables:
#Drop TABLE
	if item in statesToInsert:
		print("found a state "+str(item))
	else:
		count += 1
        session.execute("DROP TABLE " + item +";")
print("removed "+str(count))
cluster.shutdown()
