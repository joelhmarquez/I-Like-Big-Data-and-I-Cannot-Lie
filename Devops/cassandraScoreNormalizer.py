import math
import sys
import time
from cassandra.cluster import Cluster
from cassandra.query import *
cluster = Cluster(['172.31.3.194'], port=9042)
session = cluster.connect()

session.row_factory = dict_factory

statesToInsert=['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'newhampshire', 'newjersey', 'newmexico', 'newyork', 'northcarolina', 'northdakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhodeisland', 'southcarolina', 'southdakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'westvirginia', 'wisconsin', 'wyoming']

for state in statesToInsert:
	#Handle broken keyspace names
	try:
		session.set_keyspace(state)
		timeblocks = sorted(cluster.metadata.keyspaces[state].tables.keys())

		timeNow = int(time.time())/3600
		#Handle if the keyspace deosn't have tables yet
		try:
			for timeblock in timeblocks:
				if timeNow - int(timeblock) != 0:
					#General exception handling
					try:
						countQuery = "select count(*) from \"%s\" where id = \'0\';" % timeblock
						countResult = session.execute(countQuery)[0]
						if int(countResult['count']) == 0:
							dbQuery = "select * from \"%s\";" % str(timeblock)
							dbResult = []
							flaggedScore = 0
							for result in session.execute(dbQuery):
								dbResult.append(result)
								if float(result["sentimentscore"]) != 0.0:
									flaggedScore += 1
							overallScore = 100.0*(float(flaggedScore) / float(len(dbResult)))
							insertQuery = "INSERT INTO \"%s\" JSON \'{\"id\":\"0\", \"sentimentscore\":\"%s\"}\';" % (timeblock, overallScore)
							session.execute(insertQuery)

						'''
						#Debugging printstatements
						else:
							retrieveScore = "select * from \"%s\" where id = \'0\';" % timeblock
							print state, timeblock, session.execute(retrieveScore)[0]["sentimentscore"]
						'''
					
					except Exception as e:
						print e
									
		except Exception as e:
			print e

	except Exception as e:
		print e

cluster.shutdown()
