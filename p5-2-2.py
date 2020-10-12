import requests
from bs4 import BeautifulSoup

url = 'https://udn.com/news/breaknews/1'
html = requests.get(url).text
sel = '#breaknews > div.context-box__content.story-list__holder.story-list__holder--full > div> div.story-list__text'
soup = BeautifulSoup(html, 'html.parser')
target = soup.select(sel)
print(target)