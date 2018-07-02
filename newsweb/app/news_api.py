from newsapi import NewsApiClient
from datetime import date, timedelta

today_date = date.today().strftime("%Y-%m-%d")
yesterday_date = (date.today() - timedelta(1)).strftime("%Y-%m-%d")
newsapi = NewsApiClient(api_key='API_KEY')
class NewsApi(object):
	
	top_headlines = newsapi.get_top_headlines(country='in'or'us',page=1)
	
	description = []
	url = []
	image_link = []
	title = []
	sources = []
	
	for article in top_headlines['articles']:
		description.append(article['description'])
		url.append(article['url'])
		image_link.append(article['urlToImage'])
		title.append(article['title'])
		sources.append(article['source']['name'])
	
	def get_discription(self):
		return self.description

	def get_url(self):
		return self.url

	def get_image_link(self):
		return self.image_link

	def get_title(self):
		return self.title

	def get_source(self):
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



