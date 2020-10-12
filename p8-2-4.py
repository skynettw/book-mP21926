from pymongo import MongoClient
import requests, time
from bs4 import BeautifulSoup
target_url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php'

data = list()
for page in range(1, 6):
    html = requests.get(target_url.format(page)).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#pageptlist > div > div > div > div > div'
    target = soup.select(sel)
    for item in target:
        pdate = item.i.text
        title = item.a.text.strip()
        link = item.a['href']
        data.append((pdate, link, title))
    time.sleep(3)

conn = MongoClient()
db = conn.news
collection = db.nkust
for article in data[:10]:
    content = dict()
    url = article[1]
    content['date'] = article[0]
    content['title'] = article[2]
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#Dyn_2_3 > div.module.module-detail.md_style1 > div > section > div.mcont > div.mpgdetail > p:nth-child(2)'
    target = soup.select(sel)
    try:
        content['content'] = target[0].text
    except:
        content['content'] = ""
        pass
    try:
        collection.insert_one(content)
    except:
        pass
    print(content)
    time.sleep(3)
print("Done")