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
        pdate = item.i.text.strip()
        title = item.a.text.strip()
        link = item.a['href']
        data.append((pdate, link, title))
    time.sleep(3)
contents = list()
for article in data[:5]:
    content = dict()
    url = article[1]
    content['link'] = url
    print(url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#Dyn_2_3 > div.module.module-detail.md_style1 > div > section > div.mcont > div.mpgdetail p'
    target = soup.select(sel)
    content['content'] = ""
    for item in target:
        try:
            content['content'] += item.text
        except:
            content['content'] += ""
            pass
    contents.append(content)
    time.sleep(3)
print(contents)