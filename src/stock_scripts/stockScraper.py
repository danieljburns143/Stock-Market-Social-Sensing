#/usr/bin/python3

import json
import requests

class StockScraper():

	def __init__(self):
		self.apiKey = '7IG1A5W6UY6CAZQI'
		self.queryURL = 'https://www.alphavantage.co/query'
	
	def getTimeSeriesDaily(self, symbol, outputsize='compact', datatype='json'):
		payload = {'function': 'TIME_SERIES_DAILY', 'symbol': symbol, \
			'outputsize': outputsize, 'datatype': datatype, 'apikey': self.apiKey}
		return requests.get(self.queryURL, params=payload)
	
	def getTimeSeriesWeekly(self, symbol, datatype='json'):
		payload = {'function': 'TIME_SERIES_WEEKLY', 'symbol': symbol, \
			'datatype': datatype, 'apikey': self.apiKey}
		return requests.get(self.queryURL, params=payload)
	
	def getTimeSeriesMonthly(self, symbol, datatype='json'):
		payload = {'function': 'TIME_SERIES_MONTHLY', 'symbol': symbol, \
			'datatype': datatype, 'apikey': self.apiKey}
		return requests.get(self.queryURL, params=payload)
