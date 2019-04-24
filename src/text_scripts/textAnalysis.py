from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getSentimentBlob(text):
    return TextBlob(text).sentiment

def getSentimentVader(text):
    return SentimentIntensityAnalyzer().polarity_scores(text) 
