from cassandra.cluster import Cluster
cluster = Cluster(contact_point=['172.31.35.21'], port=9042)
session = cluster.connect()

session.row_factory = dict_factory        

statesToInsert=['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'newhampshire', 'newjersey', 'newmexico', 'newyork', 'northcarolina', 'northdakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhodeisland', 'southcarolina', 'southdakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'westvirginia', 'wisconsin', 'wyoming']
stateToCode = {"alabama":"Alabama","alaska":"Alaska","arizona":"Arizona","arkansas":"Arkansas","california":"California","colorado":"Colorado","connecticut":"Connecticut","delaware":"Delaware","florida":"Florida","georgia":"Georgia","hawaii":"Hawaii","idaho":"Idaho","illinois":"Illinois","indiana":"Indiana","iowa":"Iowa","kansas":"Kansas","kentucky":"Kentucky","louisiana":"Louisiana","maine":"Maine","maryland":"Maryland","massachusetts":"Massachusetts","michigan":"Michigan","minnesota":"Minnesota","mississippi":"Mississippi","missouri":"Missouri","montana":"Montana","nebraska":"Nebraska","nevada":"Nevada","newhampshire":"New Hampshire","newjersey":"New Jersey","newmexico":"New Mexico","newyork":"New York","northcarolina":"North Carolina","northdakota":"North Dakota","ohio":"Ohio","oklahoma":"Oklahoma","oregon":"Oregon","pennsylvania":"Pennsylvania","rhodeisland":"Rhode Island","southcarolina":"South Carolina","southdakota":"South Dakota","tennessee":"Tennessee","texas":"Texas","utah":"Utah","vermont":"Vermont","virginia":"Virginia","washington":"Washington","westvirginia":"West Virginia","wisconsin":"Wisconsin","wyoming":"Wyoming"}

finalMapScore = [[str('State'), str('Hate Score')]]
for state in statesToInsert:
        #Handle broken keyspace names
        try:
                session.set_keyspace(state)
                timeblocks = sorted(cluster.metadata.keyspaces[state].tables.keys())

                #Handle if the keyspace deosn't have tables yet
                try:
                        for timeblock in timeblocks:

                                session.execute("COPY \"timeblock\"(id, tweettext, lat, lng, time, location, sentimentscore, state) TO \'"+state+"."+timeblock+".txt\'")


                except:
                        print "failed to make copy of keyspaces."
        except:
                print "failes to handle keyspace name."

cluster.shutdown()