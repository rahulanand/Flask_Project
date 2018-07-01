from flask import render_template, redirect, url_for
from app import app
from app import news_api

@app.route('/home')
@app.route('/')
def index():
	news = news_api.NewsApi()
	descriptions = news.get_discription()
	urls = news.get_url()
	images = news.get_image_link()
	title = news.get_title()

	n = len(descriptions)
	return render_template('index.html',title='News Web', descriptions=descriptions, urls=urls, images=images,length=n, get_title=title)