#!/usr/bin/env python3

# Clusters tweets with similar Levenshtein distance to determine influence

import Levenshtein
import sys
import os
import json
from src.text_scripts import textAnalysis

class Cluster:
    def __init__(self, tweet, polarity):
        self.center = tweet
        self.nearby = []
        self.total_polarity = polarity

    def add_tweet(self, tweet, polarity, distance):
        self.nearby.append([tweet, polarity, distance])
        self.total_polarity += float(polarity)

def readPolarity(path="data/Canada_Goose/Canada_Goose_tweets_polarity.txt"):
    polarity = []
    with open(os.path.join(os.path.dirname(__file__),path),"r") as f:
        for line in f:
            data = json.loads(line.strip().replace('\'',"\""))
            polarity.append(data['compound'])
    return polarity

def readTweets(path="data/Canada_Goose/Canada_Goose_tweets.txt"):
    tweets = []
    with open(os.path.join(os.path.dirname(__file__),path),"r") as f:
        for line in f:
            tweets.append(line.strip())
    return tweets

def compareTweets(t1,t2):
    return Levenshtein.ratio(t1,t2)

def measureTweets(tweets):
    similarity_matrix = [[0]*len(tweets)]*len(tweets)
    for x,tweet1 in enumerate(tweets):
        for y,tweet2 in enumerate(tweets):
            similarity_matrix[x][y] = compareTweets(tweet1,tweet2)
    return similarity_matrix

def clusterTweets(similarity_matrix, bound, tweets, polarity):
    clusters = []
    clustered = []
    centers = {}
    for i,row in enumerate(similarity_matrix):
        for j, similarity in enumerate(row):
            if similarity == 1.0 and j not in (centers or clustered):
                if i not in centers.keys():
                    centers[i] = Cluster(tweets[i],polarity[i])
                else:
                    centers[i].add_tweet(tweet[j],polarity[j])
                    clustered.append[j] 
    for i in centers.keys():
        clusters.append(centers[i])
    return clusters

def main():
    tweets = readTweets()
    polarities = readPolarity()
    matrix = measureTweets(tweets)
    clustered_tweets = clusterTweets(matrix, 0.75, tweets, polarities)
    for cluster in sorted(clustered_tweets, key=lambda x: len(x.nearby)):
        print ("Text: " + str(cluster.center) + "\nPolarity:" + str(cluster.total_polarity) + "\nInfluence:" + str(len(cluster.nearby)))
        print ("\n") 

if __name__=='__main__':
    main()
