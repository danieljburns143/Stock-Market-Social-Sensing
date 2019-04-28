#!/usr/bin/env python3

import os
import json
import re
from src.stock_scripts.stockScraper import StockScraper
from src.text_scripts import textAnalysis
from src.twitter_scripts.twitterScraper import TwitterScraper
from src.heatmap_scripts.heatMapper import heatMapper

def getTweets(): 
    tweetScraper = TwitterScraper(since="2019-04-03", until="2019-04-10",
            query="coca cola")
    tweets = tweetScraper.getTweets()
    tweetfile = open(os.path.join(os.path.dirname(__file__),
        "data/Coca_Cola/Coca_Cola_tweets.txt"), "w")
    for tweet in tweets:
        tweetfile.write(tweet.text + "\n")

def getSentiment():
    sentfile = open(os.path.join(os.path.dirname(__file__),
        "data/Coca_Cola/Coca_Cola_tweets_polarity.txt"), "w")
    with open(os.path.join(os.path.dirname(__file__),
        "data/Coca_Cola/Coca_Cola_tweets.txt"),"r") as f:
        for line in f:
            sentfile.write(str(textAnalysis.getSentimentVader(line))+"\n")


def getStocks():
    stockfile = open(os.path.join(os.path.dirname(__file__),
    "data/Coca_Cola/Coca_Cola_stocks.json"), "w")
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
