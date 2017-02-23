from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def checkForHateWords(tweet):
    hateWords = set(['race','racism','discrimination','vandalism',
        'hate','slur','abuse','genocide','thug','thuggery','bigotry',
        'violence','sex','sexual', 'assault', 'bullying', 'shooting',
        'threat', 'threatening', 'kill', 'terror', 'terrorism', 'crime',
        'criminal', 'bashing', 'shaming', 'slut', 'abusive', 'nigga',
        'fuck', 'frick', 'nigger','chink'."fishface"
    ])

    for word in tweet:
        if word.lower() in hateWords:
            sentimentScore = TextBlob(tweet)
            return (True,sentimentScore.sentiment.polarity)
    return (False,0)