import pytest

from bloombergScraper import *

class TestBloombergScraper():
    def test_make_request():
        bs = BloombergScraper()
        print (bs.make_request())

    def test_make_requests():
        bs = BloombergScraper()
        bs.tickers(["AAPL", "AMZN", "GOOG"])
        if bs.make_requests() == 0:
            print (bs.executives)
        else:
            print ("Error making multiple requests.")
