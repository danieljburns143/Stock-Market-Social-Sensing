import pytest

from src.text_scripts.textAnalysis import *

class TestTextAnalysis():

	def test_getSentimentBlob(self):
		assert(getSentimentBlob('This is a good test of textblob') != None)
	
	def test_getSentimentVader(self):
		assert(getSentimentVader('This is a good test of vaderSentiment') != None)
