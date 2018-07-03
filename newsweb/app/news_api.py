from newsapi import NewsApiClient
from datetime import date, timedelta

today_date = date.today().strftime("%Y-%m-%d")
yesterday_date = (date.today() - timedelta(1)).strftime("%Y-%m-%d")
newsapi = NewsApiClient(api_key='API_KEY')

class NewsApi(object):

	def __init__(self, parameter):
		self.parameter = parameter
		self.top_headlines = newsapi.get_top_headlines(q=self.parameter,country='in')
		self.description = []
		self.url = []
		self.image_link = []
		self.title = []
		self.sources = []
		for article in self.top_headlines['articles']:
			self.description.append(article['description'])
			self.url.append(article['url'])
			self.image_link.append(article['urlToImage'])
			self.title.append(article['title'])
			self.sources.append(article['source']['name'])

	def get_description(self):
		return self.description

	def get_url(self):
		return self.url

	def get_images(self):
		return self.image_link

	def get_title(self):
		return self.title

	def get_sources(self):
		return self.sources

class CricketNews(NewsApi):
	get_every = newsapi.get_everything(q="Cricket",
											from_parameter=yesterday_date,	
											to=today_date,
											language='en',
											sort_by='relevancy',
											page=2)
	description = []
	url = []
	image_link = []
	title = []
	
	for article in get_every['articles']:
		description.append(article['description'])
		url.append(article['url'])
		image_link.append(article['urlToImage'])
		title.append(article['title'])



