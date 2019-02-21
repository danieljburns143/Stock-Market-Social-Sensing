import pytest

from stockScraper import StockScraper

class TestStockScraper():

	def test_getTimeSeriesDaily(self):
		stockScraper = StockScraper()
		statusCode = stockScraper.getTimeSeriesDaily(symbol='SQ').status_code
		assert(statusCode == 200)
	
	def test_getTimeSeriesWeekly(self):
		stockScraper = StockScraper()
		statusCode = stockScraper.getTimeSeriesWeekly(symbol='SQ').status_code
		assert(statusCode == 200)

	def test_getTimeSeriesMonthly(self):
		stockScraper = StockScraper()
		statusCode = stockScraper.getTimeSeriesMonthly(symbol='SQ').status_code
		assert(statusCode == 200)
