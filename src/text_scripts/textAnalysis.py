#!/usr/bin/env python3

from textblob import TextBlob

def getSentiment(text):
	return TextBlob(text).sentiment
