import pytest

from src.text_scripts.textAnalysis import *

class TestTextAnalysis():

	def test_getSentiment(self):
		assert(getSentiment('This is a good test of textblob') != None)
