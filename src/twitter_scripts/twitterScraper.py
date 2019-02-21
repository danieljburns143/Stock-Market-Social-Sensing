from src.twitter_scripts.GetOldTweets_python import got3

class TwitterScraper():

	def __init__(self, username=None, since=None, until=None, query=None, topTweets=False, \
		near=None, within=None, maxTweets=None):
		self._username = username
		self._since = since
		self._until = until
		self._query = query
		self._topTweets = topTweets
		self._near = near
		self._within = within
		self._maxTweets = maxTweets
	
	def getTweets(self):
		tweetCriteria = got3.manager.TweetCriteria()
		if self.username: tweetCriteria.setUsername(self.username)
		if self.query: tweetCriteria.setQuerySearch(self.query)
		if self.since: tweetCriteria.setSince(self.since)
		if self.until: tweetCriteria.setUntil(self.until)
		if self.near: tweetCriteria.setNear(self.near)
		if self.within: tweetCriteria.setWithin(self.within)
		if self.topTweets: tweetCriteria.setTopTweets(self.topTweets)
		if self.maxTweets: tweetCriteria.setMaxTweets(self.maxTweets)
		return got3.manager.TweetManager.getTweets(tweetCriteria)
	
	def getMostFavoritedTweets(self, numTweets):
		tweets = self.getTweets()
		topTweets = sorted(tweets, key=lambda x: x.favorites)[-numTweets:]
	
	# Properties
	@property
	def username(self): return self._username

	@property
	def since(self): return self._since

	@property
	def until(self): return self._until

	@property
	def query(self): return self._query

	@property
	def topTweets(self): return self._topTweets

	@property
	def near(self): return self._near

	@property
	def within(self): return self._within

	@property
	def maxTweets(self): return self._maxTweets

	# Setters
	@username.setter
	def username(self, value):
		if type(value) == str: self._username = value
		else: raise TypeError('username must be str')

	@since.setter
	def since(self, value):
		if type(value) == str: self._since = value
		else: raise TypeError('since must be str')

	@until.setter
	def until(self, value):
		if type(value) == str: self._until = value
		else: raise TypeError('until must be str')
	
	@query.setter
	def query(self, value):
		if type(value) == str: self._query = value
		else: raise TypeError('query must be str')
	
	@topTweets.setter
	def topTweets(self, value):
		if type(value) == bool: self._topTweets = value
		else: raise TypeError('topTweets must be bool')
	
	@near.setter
	def near(self, value):
		if type(value) == str: self._near = value
		else: raise TypeError('near must be str')
	
	@within.setter
	def within(self, value):
		if type(value) == str: self._within = value
		else: raise TypeError('within must be str')
	
	@maxTweets.setter
	def maxTweets(self, value):
		if type(value) == int: self._maxTweets = value
		else: raise TypeError('maxTweets must be int')
