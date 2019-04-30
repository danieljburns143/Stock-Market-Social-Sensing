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

    def add_tweet(self, tweet_num, tweet, polarity, distance):
        self.nearby.append([tweet_num, tweet, polarity, distance])
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
            if textAnalysis.getLanguage(line) == "en":
                tweets.append(line.strip())
    return tweets

def compareTweets(t1,t2):
    return round(Levenshtein.ratio(t1,t2),3)

def measureTweets(tweets):
    similarity_matrix = [[0 for x in range(len(tweets))] for y in range(len(tweets))]
    for x,tweet1 in enumerate(tweets):
        for y,tweet2 in enumerate(tweets):
            similarity_matrix[x][y] = compareTweets(tweet1,tweet2)
    return similarity_matrix

def clusterTweets(similarity_matrix, bound, tweets, polarity):
    centers = {}
    for i,row in enumerate(similarity_matrix):
        centers[i] = Cluster(tweets[i], polarity[i])
        for j, similarity in enumerate(row):
            if float(similarity) > float(bound):
                centers[i].add_tweet(j, tweets[j], polarity[j], similarity) 
    return centers

def filter_cluster(clusters, matrix):
    new_clusters = clusters
    for x,cluster1 in enumerate(clusters):
        for y,cluster2 in enumerate(clusters):
            for a,element1 in enumerate(cluster1.nearby):
                for b,element2 in enumerate(cluster2.nearby):
                    if x != y and element1[0] == element2[0]:
                        if element1[3] <= element2[3]:
                            new_clusters[x].nearby.remove(element1)
                            new_clusters[x].total_polarity -= element1[1]
                        elif element1[3] > element2[3]:
                            new_clusters[y].nearby.remove(element2)
                            new_clusters[y].total_polarity -= element2[1]
    return new_clusters

def main():
    tweets = readTweets()
    polarities = readPolarity()
    matrix = measureTweets(tweets)
    clustered = clusterTweets(matrix, 0.75, tweets, polarities)
    i = 0
    clusters = []
    for item in clustered.keys():
        if clustered[item].total_polarity != 0.0:
            clusters.append(clustered[item])
    filtered_clusters = filter_cluster(clusters, matrix)
    for item in sorted(filtered_clusters, key=lambda x:len(x.nearby), reverse=True):
        print (str(item.center) + " : " + str(item.total_polarity) + " : " + str(len(item.nearby)))
        i+=1 
        if i>10:
            break
    #for cluster in sorted(clustered_tweets, key=lambda x: len(x.nearby)):
    #    print ("Text: " + str(cluster.center) + "\nPolarity:" + str(cluster.total_polarity) + "\nInfluence:" + str(len(cluster.nearby)))
    #    print ("\n") 

if __name__=='__main__':
    main()
