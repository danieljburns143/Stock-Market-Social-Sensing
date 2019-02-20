import pytest

from bloombergScraper import *

class TestBloombergScraper():

    def test_make_request(self):
        bs = BloombergScraper()
        bs.set_server()
        print (bs.make_request())

    def test_make_requests(self):
        bs = BloombergScraper()
        bs.set_server()
        bs.set_tickers(["AAPL", "AMZN", "GOOG"])
        if bs.make_requests() == 0:
            print (bs.executives)
        else:
            print ("Error making multiple requests.")

