#!/usr/bin/env python3

from GetOldTweets_python import got3

class TwitterScraper():

	def __init__(self, username=None, since=None, until=None, query=None, topTweets=False, \
		near=None, within=None, maxTweets=None):
		self.username = username
		self.since = since
		self.until = until
		self.query = query
		self.topTweets = topTweets
		self.near = near
		self.within = within
		self.maxTweets = maxTweets
	
	def getTweets(self):
		tweetCriteria = got3.manager.TweetCriteria()
		if self.username: tweetCriteria.setUsername(self.username)
		if self.since: tweetCriteria.setSince(self.since)
		if self.until: tweetCriteria.setUntil(self.until)
		if self.query: tweetCriteria.setQuerySearch(self.query)
		if self.topTweets: tweetCriteria.setTopTweets(self.topTweets)
		if self.near: tweetCriteria.setNear(self.near)
		if self.within: tweetCriteria.setWithin(self.within)
		if self.maxTweets: tweetCriteria.setMaxTweets(self.maxTweets)
		return got3.manager.TweetManager.getTweets(tweetCriteria)

if __name__ == '__main__':
	twitterScraper = TwitterScraper()
	twitterScraper.username = 'elonmusk'
