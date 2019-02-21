#!/usr/bin/env python3

import json

from src.stock_scripts import stockScraper
from src.text_scripts import textAnalysis
from src.twitter_scripts import twitterScraper

def getTopTweets(): 
	tweetScraper = twitterScraper.TwitterScraper(since="2018-12-11", until="2018-12-12", \
		query="tesla")
	topTweets = tweetScraper.getTopTweets(10)
	for tweet in topTweets:
		if tweet.id in influencers.keys():
			influencers[tweet.id].append(tweet)
		else: 
			influencers[tweet.id] = [tweet]

def main():
	with open('./data/Tesla/Tesla_stock.json', 'r') as f:
		json_data = json.load(f)
	getTopTweets()
	print(influencers)

if __name__ == '__main__':
	influencers = {}
	main()
