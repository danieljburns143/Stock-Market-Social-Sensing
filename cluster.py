#!/usr/bin/env python3

# Clusters tweets with similar Levenshtein distance to determine influence

import Levenshtein
import sys
from src.text_scripts import textAnalysis

class Cluster:
    def __init__(self, tweet):
        self.center = tweet
        self.nearby = {}
        self.avg_polarity = 0

    def add_tweet(self, tweet, polarity, distance):
        self.nearby[tweet] = [polarity, distance]
        self.avg_polarity = (len(nearby.keys()-1)*self.avg_polarity + polarity) / (len(nearby.keys()))

    def readPolarity(path="data/Canada_Goose/Canada_Goose_tweets_polarity.txt"):
        polarity = []
        with open(os.path.join(os.path.dirname(__file__),path),"r") as f:
            for line in f:
                polarity.append(line.strip())

    def readTweets(path="data/Canada_Goose/Canada_Goose_tweets.txt"):
        tweets = []
        with open(os.path.join(os.path.dirname(__file__),path),"r") as f:
            for line in f:
                tweets.append(line.strip())

    def compareTweets(t1,t2):
        return Levenshtein.ratio(t1,t2)

    def measureTweets(tweets):
        similarity_matrix = [[0]*len(tweets)]*len(tweets)
        for x,tweet1 in enumerate(tweets):
            for y,tweet2 in enumerate(tweets):
                similarity_matrix[x][y]= compareTweets(tweet1,tweet2)
        return similarity_matrix

    def clusterTweets(similarity_matrix, bound, tweets, polarity):
        clustered = []
        clusters = []
        for i,row in enumerate(similarity_matrix):
            for j, similarity in enumerate(row):
                if similarity > bound and i not in clustered:
                    center = Cluster(tweets[i])
                    center.add_tweet(tweets[j], polarity[j], similarity)
                    clustered.append(i)
                    clusters.append(center)
                else if similarity > bound:
                    center.add_tweet(tweets[j],polarity[j], similarity)
        return clusters

def main():
    tweets = readTweets()
    polarities = readPolarity()
    matrix = measureTweets(tweets)
    clustered_tweets = clusterTweets(matrix, 0.75, tweets, polarities)
    for cluster in sorted(clustered_tweets, key=lambda x: len(x.nearby)):
        print ("Text: " + cluster.center + "\nPolarity: " cluster.avg_polarity + "\nInfluence: " + len(cluster.nearby))
        
if __name__=='__main__':
    main()
