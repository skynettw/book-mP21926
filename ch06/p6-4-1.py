import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
session = requests.Session()
payload = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes"
}
session.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)
html = session.get(url).text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.title')
for title in titles:
    print(title.a.text)
    print(title.a['href'])