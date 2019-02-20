import pytest

from twitterScraper import TwitterScraper

class TestTwitterScraper():

	def test_username(self):
		twitterScraper = TwitterScraper()
		twitterScraper.username = 'elonmusk'
		twitterScraper.maxTweets = 1
		tweets = twitterScraper.getTweets()
		assert(tweets != None)
		assert(tweets[0].username == 'elonmusk')

	def test_maxTweets(self):
		twitterScraper = TwitterScraper()
		twitterScraper.username = 'elonmusk'
		twitterScraper.maxTweets = 2
		tweets = twitterScraper.getTweets()
		assert(tweets != None)
		assert(len(tweets) == 2)

	def test_since_until(self):
		twitterScraper = TwitterScraper()
		twitterScraper.username = 'elonmusk'
		twitterScraper.since = '2018-08-06'
		twitterScraper.until = '2018-08-08'
		tweets = twitterScraper.getTweets()
		assert(tweets != None)
	
	def test_query(self):
		twitterScraper = TwitterScraper()
		twitterScraper.since = '2018-08-08'
		twitterScraper.until = '2018-08-12'
		twitterScraper.query = 'cars'
		twitterScraper.maxTweets = 1
		tweets = twitterScraper.getTweets()
		assert(tweets != None)
	
	def test_topTweets(self):
		twitterScraper = TwitterScraper()
		twitterScraper.username = 'elonmusk'
		twitterScraper.topTweets = True
		twitterScraper.maxTweets = 2
		tweets = twitterScraper.getTweets()
		assert(tweets != None)
	
	def test_location(self):
		twitterScraper = TwitterScraper()
		twitterScraper.location = 'Indiana'
		twitterScraper.within = '20mi'
		twitterScraper.maxTweets = 4
		tweets = twitterScraper.getTweets()
		assert(tweets != None)
