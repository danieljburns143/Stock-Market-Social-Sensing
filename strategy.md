# Process
1. Import our scripts. Might be worth initializing a database using pandadb to store multiple tables of info.
2. Given list of tickers, request executives.
3. For each executive, collect their tweets if they can be found on twitter.
4. For each tweet, perform sentiment analysis.
5. Compare sentiment analysis with stock movement following tweet. 
6. If matching, increase "influence" indicator. Else, don't. 
7. Return influence indicator for individual alongside tweet and timing of stock movement. 
