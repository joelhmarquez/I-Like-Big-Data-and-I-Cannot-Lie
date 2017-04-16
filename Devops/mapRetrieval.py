import math
import sys
import time
from cassandra.cluster import Cluster
from cassandra.query import *
cluster = Cluster(['172.31.35.21'], port=9042)
session = cluster.connect()

session.row_factory = dict_factory

statesToInsert=['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'newhampshire', 'newjersey', 'newmexico', 'newyork', 'northcarolina', 'northdakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhodeisland', 'southcarolina', 'southdakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'westvirginia', 'wisconsin', 'wyoming']
stateToCode = {"alabama":"US-AL","alaska":"US-AK","arizona":"US-AZ","arkansas":"US-AR","california":"US-CA","colorado":"US-CO","connecticut":"US-CT","delaware":"US-DE","florida":"US-FL","georgia":"US-GA","hawaii":"US-HI","idaho":"US-ID","illinois":"US-IL","indiana":"US-IN","iowa":"US-IA","kansas":"US-KS","kentucky":"US-KY","louisiana":"US-LA","maine":"US-ME","maryland":"US-MD","massachusetts":"US-MA","michigan":"US-MI","minnesota":"US-MN","mississippi":"US-MS","missouri":"US-MO","montana":"US-MT","nebraska":"US-NE","nevada":"US-NV","newhampshire":"US-NH","newjersey":"US-NJ","newmexico":"US-NM","newyork":"US-NY","northcarolina":"US-NC","northdakota":"US-ND","ohio":"US-OH","oklahoma":"US-OK","oregon":"US-OR","pennsylvania":"US-PA","rhodeisland":"US-RI","southcarolina":"US-SC","southdakota":"US-SD","tennessee":"US-TN","texas":"US-TX","utah":"US-UT","vermont":"US-VT","virginia":"US-VA","washington":"US-WA","westvirginia":"US-WV","wisconsin":"US-WI","wyoming":"US-WY"}
          
finalMapScore = [['State', 'Hate Score']]
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
						countResult = float("%.2f" % float(session.execute(countQuery)[0]['sentimentscore']))

					except Exception as e:
						countResult = 0.00
						print "Query Error: %s" % e
									
		except Exception as e:
			countResult = 0.00
			print e

	except Exception as e:
		countResult = 0.00
		print e



	finalMapScore.append([state, countResult])

print finalMapScore
cluster.shutdown()
