#/usr/bin/env python3

import json
import re
from src.stock_scripts import stockScraper
from src.text_scripts import textAnalysis
from src.twitter_scripts.twitterScraper import TwitterScraper
from src.heatmap_scripts.heatMapper import heatMapper

def getTweets(): 
	tweetScraper = TwitterScraper(since="2019-02-21", until="2019-02-28", query="tesla")
	tweets = tweetScraper.getTweets()
	for tweet in tweets:
		print(textAnalysis.getSentiment(tweet.text).polarity)

def main():
	getTweets()

if __name__ == '__main__':
        main()
