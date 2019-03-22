#!/usr/bin/env python3

import json
import re
from src.stock_scripts.stockScraper import StockScraper
from src.text_scripts import textAnalysis
from src.twitter_scripts.twitterScraper import TwitterScraper
from src.heatmap_scripts.heatMapper import heatMapper

def getTweets(): 
	tweetScraper = TwitterScraper(since="2019-02-28", until="2019-03-07", query="canada goose")
	tweets = tweetScraper.getTweets()
	for tweet in tweets:
		print(textAnalysis.getSentiment(tweet.text).polarity)

def getStocks():
	stockScraper = StockScraper()
	stockPrices = stockScraper.getTimeSeriesDaily('GOOS')
	print(stockPrices.text)

def main():
	getTweets()

if __name__ == '__main__':
        main()
