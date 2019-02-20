import src.twitter_scripts.twitterScraper
import src.text_scripts.extAnalysis 
import json

def main(args):
	json_data = open("/data/Tesla/Tesla_stock.json").read()
	data = json.loads(json_data)
	print (data)

if __name__=="__main__":
	main()