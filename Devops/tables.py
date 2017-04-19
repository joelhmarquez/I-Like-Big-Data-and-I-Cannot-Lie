from cassandra.cluster import Cluster
cluster = Cluster(contact_point=['172.31.35.21'], port=9042)
session = cluster.connect()

statesToInsert = {
        'AK',
        'AL',
        'AR',
        'AZ',
        'CA',
        'CO',
        'CT',
        'DC',
        'DE',
        'FL',
        'GA',
        'HI',
        'IA',
        'ID',
        'IL',
        'IN',
        'KS',
        'KY',
        'LA',
        'MA',
        'MD',
        'ME',
        'MI',
        'MN',
        'MO',
        'MS',
        'MT',
        'NC',
        'ND',
        'NE',
        'NH',
        'NJ',
        'NM',
        'NV',
        'NY',
        'OH',
        'OK',
        'OR',
        'PA',
        'RI',
        'SC',
        'SD',
        'TN',
        'TX',
        'UT',
        'VA',
        'VI',
        'VT',
        'WA',
        'WI',
        'WV',
        'WY'
}

for item in statesToInsert:
        #insert into the table
        session.execute("CREATE KEYSPACE IF NOT EXISTS " + item + " WITH replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };")


cluster.shutdown()