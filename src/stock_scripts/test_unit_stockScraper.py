#!/usr/bin/python3

import pytest
from src.stock_scripts.stockScraper import stockScraper

class TestStockScraper():

	def test_getTimeSeriesDaily(self):
		stockScraper = StockScraper()
		r = stockScraper.getTimeSeriesDaily(symbol='SQ')
                assert(r.status_code == 200)
	
	def test_getTimeSeriesWeekly(self):
		stockScraper = StockScraper()
		r = stockScraper.getTimeSeriesWeekly(symbol='SQ')
		assert(r.statusCode == 200)

	def test_getTimeSeriesMonthly(self):
		stockScraper = StockScraper()
		r = stockScraper.getTimeSeriesMonthly(symbol='SQ')
		assert(r.statusCode == 200)
