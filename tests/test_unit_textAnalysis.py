import pytest
from ..src.textAnalysis import *

class TestTextAnalysis():

	def test_getSentiment(self):
		assert(getSentiment('This is a good test of textblob') != None)
