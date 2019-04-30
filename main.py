#!/usr/bin/env python3

import json
import re
from src.stock_scripts.stockScraper import StockScraper
from src.text_scripts import textAnalysis
from src.twitter_scripts.twitterScraper import TwitterScraper
from src.heatmap_scripts.heatMapper import heatMapper


def getTweets(): 
    tweetScraper = TwitterScraper(since="2019-04-08", until="2019-04-12", query="visa")
    tweets = tweetScraper.getTweets()
    for tweet in tweets:
        print(tweet.text)

def getStocks():
    stockScraper = StockScraper()
    stockPrices = stockScraper.getTimeSeriesDaily('GOOS')
    print(stockPrices.text)

def main():
    getStocks()

if __name__ == '__main__':
    main()
