#!/usr/bin/env python3

import json

from GetOldTweets_python import *

from src.twitter_scripts.twitterScraper import *
import src.text_scripts.textAnalysis 

def main():
	with open('./data/Tesla/Tesla_stock.json', 'r') as f:
		json_data = json.load(f)
	print (json_data)
	getTopTweets()
	print (influencers)


def getTopTweets(): 
	twitterScraper = TwitterScraper(since="2018-12-11", until="2018-12-12", query="tesla")
	ts = twitterScraper.getTweets()
	topTweets = sorted(ts, key = lambda x: x.favorites)[-10:]
	for tweet in topTweets:
		if tweet.id in influencers.keys():
			influencers[tweet.id].append(tweet)
		else: 
			influencers[tweet.id] = [tweet]

if __name__ == '__main__':
	influencers = {}
	main()
