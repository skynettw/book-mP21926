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
print(data)