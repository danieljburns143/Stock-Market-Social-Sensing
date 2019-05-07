#!/usr/bin/env python3

import os
import json
import re
from src.stock_scripts.stockScraper import StockScraper
from src.text_scripts import textAnalysis
from src.twitter_scripts.twitterScraper import TwitterScraper
from src.heatmap_scripts.heatMapper import heatMapper

def getTweets(): 
    tweetScraper = TwitterScraper(since="2019-02-28", until="2019-03-07",
            query="canada goose")
    tweets = tweetScraper.getTweets()
    tweetfile = open(os.path.join(os.path.dirname(__file__),
        "data/Canada_Goose/Canada_Goose_tweets.txt"), "w")
    for tweet in tweets:
        tweetfile.write(tweet.text + "\n")

def getSentiment():
    sentfile = open(os.path.join(os.path.dirname(__file__),
        "data/Canada_Goose/Canada_Goose_tweets_polarity.txt"), "w")
    with open(os.path.join(os.path.dirname(__file__),
        "data/Canada_Goose/Canada_Goose_tweets.txt"),"r") as f:
        for line in f:
            sentfile.write(str(textAnalysis.getSentimentVader(line))+"\n")


def getStocks():
    stockfile = open(os.path.join(os.path.dirname(__file__),
    "data/Canada_Goose/Canada_Goose_stocks.json"), "w")
    stockScraper = StockScraper()
    stockPrices = stockScraper.getTimeSeriesDaily('KO')
    for line in stockPrices.text:
        stockfile.write(line)

def main():
    getTweets()
    getSentiment()
    getStocks()

if __name__ == '__main__':
    main()
