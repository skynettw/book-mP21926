import requests, json
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://udn.com/news/breaknews/1'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all(class_='story-list__text')
headlines = list()
for link in links:
    title = link.find('h3')
    try:
        item = dict()
        item['title'] = title.a['title']
        if not title.a['href'].startswith('http'):
            item['link'] = "https://udn.com{}".format(title.a['href'])
        else:
            item['link'] = title.a['href']
        headlines.append(item)
    except:
        pass
now = datetime.now()
filename = now.strftime("%y-%m-%d-%H-%M-%S.json")
with open(filename, "w", encoding='utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(headlines, fp)
print(headlines)
