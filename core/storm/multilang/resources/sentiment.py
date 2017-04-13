from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import math
import storm
import json
hateWords = set()
hateFile = open("resources/hatewords.txt", "r")
for word in hateFile:
    hateWords.add(word.rstrip())
hateFile.close()

#For this to work, it is necessary to use the following command:
#pip install textblob
#The test.txt uses hate words to say positive stuff about racism, etc
#The score will be greater than 0 because the statement is positive
#even though the content is not.


class tweetFilteredSentiment(storm.BasicBolt):
    global hateWords
    
    def process(self,tup):
    	tweet = tup.values[0]
    	tweet['tweettext'] = tweet['text']
    	del tweet['text']
    	tweet['sentimentscore'] = str(self.checkForHateWords(tweet['tweettext']))
    	storm.emit([tweet])

    def checkForHateWords(self,tweet):
        for word in tweet.split():
            if word.lower() in hateWords:
                score = TextBlob(tweet)
                return abs(score.sentiment.polarity)
        return 0

tweetFilteredSentiment().run()
