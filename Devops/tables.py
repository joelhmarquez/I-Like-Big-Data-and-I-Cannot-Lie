from cassandra.cluster import Cluster
cluster = Cluster(['172.31.3.194'], port=9042)
try:
        session = cluster.connect()
except:
        print('failed to connect')
statesToInsert={
    'alabama',
    'alaska',
    'arizona',
    'arkansas',
    'california',
    'colorado',
    'connecticut',
    'delaware',
    'florida',
    'georgia',
    'hawaii',
    'idaho',
    'illinois',
    'indiana',
    'iowa',
    'kansas',
    'kentucky',
    'louisiana',
    'maine',
    'maryland',
    'massachusetts',
    'michigan',
    'minnesota',
    'mississippi',
    'missouri',
    'montana',
    'nebraska',
    'nevada',
    'newhampshire',
    'newjersey',
    'newmexico',
    'newyork',
    'northcarolina',
    'northdakota',
    'ohio',
    'oklahoma',
    'oregon',
    'pennsylvania',
    'rhodeisland',
    'southcarolina',
    'southdakota',
    'tennessee',
    'texas',
    'utah',
    'vermont',
    'virginia',
    'washington',
    'westvirginia',
    'wisconsin',
    'wyoming'
}

for item in statesToInsert:
        try:
        #insert into the table
                session.execute("CREATE KEYSPACE IF NOT EXISTS " + item + " WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };")
        except:
                print "database not working: %s" % item