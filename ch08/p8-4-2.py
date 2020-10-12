from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
url = 'https://tw.stock.yahoo.com/news_list/url/d/e/N1.html'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
titles_sel = '#newListTable span.mbody'
titles = soup.select(titles_sel)
timestamp_sel = '#newListTable span.t1'
timestamp = soup.select(timestamp_sel)
data = list()
for item, ts in zip(titles, timestamp):
    temp = dict()
    if item.a != None:
        temp['content'] = item.a['href']
    else:
        temp['title'] = item.text
    temp['datetime'] = ts.text
    data.append(temp)

conn = MongoClient()
db = conn.news
collection = db.yahoo
for item in data:
    try:
        collection.insert_one(item)
        print(item['title'])
    except:
        pass
print("Done")