#/usr/bin/env python3

import json
import re
from src.stock_scripts import stockScraper
from src.text_scripts import textAnalysis
from src.twitter_scripts.twitterScraper import TwitterScraper
from src.heatmap_scripts.heatMapper import heatMapper

def getStocksDaily(symbol, timeStart, timeEnd):
        ss = stockScraper.StockScraper()
        data = ss.getTimeSeriesDaily(symbol).json()
        record = False
        shortenedData = {}
        for entry in data["Time Series (Daily)"]:
            if (record): shortenedData[entry] = data["Time Series (Daily)"][entry]    
            if (entry == timeEnd): record = True
            if (entry == timeStart): break
        if len(shortenedData)==0:
            print("No data found for " + symbol + " between " + timeStart + " and " + timeEnd+ ". This time period may be when the market is closed.")
        else: return shortenedData

def getTopTweets(query, timeStart, timeEnd): 
        influencers = {}
        tweetScraper = TwitterScraper(since=timeStart, until=timeEnd, query=query)
        topTweets = tweetScraper.getMostFavoritedTweets(10)
        return topTweets
#            if tweet.id in influencers.keys():
#                influencers[tweet.id].append(tweet)
#            else: 
#                influencers[tweet.id] = [tweet]
#        return influencers

def main():
        #stocks = open("stocks.txt","w")
        #stockTSLA = getStocksDaily("TSLA", "2018-12-10","2018-12-14") 
        #stockAMZN = getStocksDaily("AMZN","2018-10-22","2018-10-25")
        #print ("\nTSLA") 
        #for stock in stockTSLA.keys():
        #    file.write(stock + "," + stockTSLA[stock])
        #print ("\nAMZN")
        #for stock in stockAMZN:
        #    file.write(stock + "," + stockTSLA[stock])
        #x = getTopTweets("tesla","2018-12-11","2018-12-12")
        x = getTopTweets("amazon","2018-10-23","2018-10-24")#2018-10-23 - 2018-10-24
        for tweet in x:
            print ("--")
            print (tweet.text.strip())
            print ("--")
if __name__ == '__main__':
        main()
