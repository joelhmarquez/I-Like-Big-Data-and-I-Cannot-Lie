from cassandra.cluster import Cluster
from cassandra.query import *

import json

statesToInsert=['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'newhampshire', 'newjersey', 'newmexico', 'newyork', 'northcarolina', 'northdakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhodeisland', 'southcarolina', 'southdakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'westvirginia', 'wisconsin', 'wyoming']

CREATE_COLUMNS = "id text PRIMARY KEY, tweettext text, lat text, lng text, time text, location text, sentimentscore text, state text"

cassandraCluster = Cluster(["172.31.35.21"], port=9042)
elassandraCluster = Cluster(["172.31.3.194"], port=9042)


cassandraSession = cassandraCluster.connect()
cassandraSession.row_factory = dict_factory

elassandraSession = elassandraCluster.connect()

for state in statesToInsert:
	try:
		cassandraSession.set_keyspace(state)
		elassandraSession.set_keyspace(state)

		timeblocks = sorted(cassandraCluster.metadata.keyspaces[state].tables.keys())

		try:
			for timeblock in timeblocks:
				rowRetrieval = "Select * From \"%s\";" % str(timeblock)
				for result in cassandraSession.execute(rowRetrieval):
					try:
						result['tweettext'] = result['tweettext'].replace("'","").replace("\"","")

					except Exception as e:
						error = e
					insertQuery = "INSERT INTO \""+str(timeblock)+"\" (id, tweettext, lat, lng, time, location, sentimentscore, state) VALUES (\'"+str(result['id'])+"\',\'"+result['tweettext']+"\',\'"+str(result['lat'])+"\',\'"+str(result['lng'])+"\',\'"+str(result['time'])+"\',\'"+str(result['location'])+"\',\'"+str(result['sentimentscore'])+"\',\'"+str(result['state'])+"\');"
					#insertQuery = "INSERT INTO \""+str(timeblock)+"\" JSON " + json.loads(result)
					try:
						elassandraSession.execute(insertQuery)

					except Exception as e:
						createTable = "Create Table \""+str(timeblock)+"\"("+CREATE_COLUMNS+");"

						try:
							elassandraSession.execute(createTable)
							try:
								elassandraSession.execute(insertQuery)
							except Exception as e:
								error = "Unable to insert with query: %s" % insertQuery
						except Exception as e:
							error = "Unable to create table with query: %s" % createTable
			
		except Exception as e:
			print "Failure in iteration of timeblocks"
			print e

	except Exception as e:
		print "Failed to set keyspace to %s" % state
		print e
