import requests
from bs4 import BeautifulSoup
url = 'https://www.bagong.cn/dog/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

photos = soup.find_all('img')
for photo in photos:
    if photo['src'].startswith('http'):
        print(photo['src'])
