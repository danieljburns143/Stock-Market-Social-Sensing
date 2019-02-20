#!/usr/bin/env python3

import src.twitter_scripts.twitterScraper
import src.text_scripts.textAnalysis 
import json

def main():
	with open('./data/Tesla/Tesla_stock.json', 'r') as f:
		json_data = json.load(f)
	print (json_data)

if __name__=="__main__":
	main()
