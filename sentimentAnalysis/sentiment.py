from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import math

#For this to work, it is necessary to use the following command:
#pip install textblob
#The test.txt uses hate words to say positive stuff about racism, etc
#The score will be greater than 0 because the statement is positive
#even though the content is not.

hateWords = set()

def normalizeText(tweet):
    tempString.deepcopy(tweet)
    # Do tolkenization and normalization of tweet
    return tempString

def checkForHateWords(tweet):
    #normalized = normalizeText(tweet)
    for word in tweet.split():
        if word.lower() in hateWords:
            sentimentScore = TextBlob(tweet)
            return (True,abs(sentimentScore.sentiment.polarity))
    return (False,0)

def loadHateWords():
    hateWords = set()
    hateFile = open("hate.txt", "r")
    for word in hateFile:
        hateWords.add(word.rstrip())
    print(hateWords)
    hateFile.close()


# The main function will need to be removed when
# integrating with Storm's java program.
def main():
    loadHateWords()
    testSentiment = open("test.txt","r")
    for line in testSentiment:
        result,score = checkForHateWords(line)
        if result:
            print("{} score:{}".format(line.rstrip(),score))
    testSentiment.close()

main()