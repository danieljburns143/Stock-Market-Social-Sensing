import pytest

from ..src.twitter_scripts.GetOldTweets_python import got3

from ..src.twitter_scripts.twitterScraper import TwitterScraper

class TestTextAnalysis():

	def test_setUsername(self):
		twitterScraper = TwitterScraper()
		twitterScraper.username = 'barackobama'
		assert(twitterScraper.getTweets() != None)
