import math
import sys
import time
from cassandra.cluster import Cluster
from cassandra.query import *
cluster = Cluster(['172.31.35.21'], port=9042)
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
						countQuery = "select \"sentimentscore\" from \"%s\" where id = \'0\';" % timeblock
						countResult = str(session.execute(countQuery)[0]['sentimentscore'])

					except Exception as e:
						countResult = "0.0"
						print "Query Error: %s" % e
									
		except Exception as e:
			countResult = "0.0"
			print e

	except Exception as e:
		countResult = "0.0"
		print e



	print timeblock, countResult, state

cluster.shutdown()
