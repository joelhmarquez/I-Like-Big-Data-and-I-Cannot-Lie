
#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *
import json
import ../sentimentAnalysis/sentiment.py

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = "nigger", lang="en")

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
file = open("tweets.txt", "w")
#json.dump(query,file)
for result in query["statuses"]:
	json.dump(result,file)
	file.write("\n\n")
	# print "{}\n".format(result)
	print "Created at: {}  User Screen Name: {}  Text: {} \n\n".format(result["created_at"], result["user"]["screen_name"], result["text"].encode("ascii", "ignore"))
	

file.close()