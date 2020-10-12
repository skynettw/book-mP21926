import requests, time, json
from bs4 import BeautifulSoup
from datetime import datetime
target = 'https://tw.appledaily.com/new/realtime/{}'

titles = list()
for page in range(1, 11):
    url = target.format(page)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#maincontent > div.thoracis > div.abdominis.rlby.clearmen > ul > li.rtddt > a'
    data = soup.select(sel)
    for item in data:
        title = dict()
        title['time'] = item.time.text
        title['title'] = item.h1.text
        title['link'] = item['href']
        titles.append(title)
    time.sleep(3)
for title in titles:
    try:
        url = title['link']
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        sel = '#article-header > header > div > h2 > span'
        target = soup.select(sel)
        print(target[0].text)
        title['title'] = target[0].text
    except:
        pass
    time.sleep(3)
    
now = datetime.now()
filename = now.strftime("news-%y-%m-%d-%H-%M-%S.json")
with open(filename, "w", encoding='utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)