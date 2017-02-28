from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

#For this to work, it is necessary to use the following command:
#pip install textblob
#The test.txt uses hate words to say positive stuff about racism, etc
#The score will be greater than 0 because the statement is positive
#even though the content is not.

def checkForHateWords(tweet):
    hateWords = set(['race','racism','discrimination','vandalism',
        'hate','slur','abuse','genocide','thug','thuggery','bigotry',
        'violence','sex','sexual', 'assault', 'bullying', 'shooting',
        'threat', 'threatening', 'kill', 'terror', 'terrorism', 'crime',
        'criminal', 'bashing', 'shaming', 'slut', 'abusive', 'nigga',
        'fuck', 'frick', 'nigger','chinks',"fishface"
    ])

    for word in tweet.split():
        if word.lower() in hateWords:
            sentimentScore = TextBlob(tweet)
            return (True,sentimentScore.sentiment.polarity)
    return (False,0)


def main():
    testSentiment = open("test.txt","r")
    for line in testSentiment:
        result,score = checkForHateWords(line)
        if result:
            print("{} score:{}".format(line,score))

main()