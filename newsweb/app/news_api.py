from newsapi import NewsApiClient


class NewsApi(object):
	newsapi = NewsApiClient(api_key='b3fd0106d80644ad8385e25ddd10aef6')
	top_headlines = newsapi.get_top_headlines(country='in')
	
	description = []
	url = []
	image_link = []
	title = []
	
	for article in top_headlines['articles']:
		description.append(article['description'])
		url.append(article['url'])
		image_link.append(article['urlToImage'])
		title.append(article['title'])

	def get_discription(self):
		return self.description

	def get_url(self):
		return self.url

	def get_image_link(self):
		return self.image_link

	def get_title(self):
		return self.title



