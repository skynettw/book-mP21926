import requests, time
from bs4 import BeautifulSoup
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
print(titles)