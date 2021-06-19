from bs4 import BeautifulSoup as bs, Comment
from pip._vendor import requests as rq

def extractSuns():
	perGameHashMap = {}
	websiteURL = 'https://www.basketball-reference.com/playoffs/2021-nba-western-conference-semifinals-nuggets-vs-suns.html'
	pageInstance = rq.get(websiteURL)

	soup = bs(pageInstance.content, 'html.parser')
	