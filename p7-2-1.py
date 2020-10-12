import requests, time, sqlite3
from bs4 import BeautifulSoup
url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php?Lang=zh-tw'
titles = list()
for page in range(11, 12):
    html = requests.get(url.format(page)).text
    soup = BeautifulSoup(html, 'html.parser')
    sel = '#pageptlist > div > div > div > div > div > a'
    data = soup.select(sel)
    for item in data:
        titles.append((item['title'], item['href']))
    time.sleep(3)
db = sqlite3.connect('headlines.db')
cur = db.cursor()
sql = "insert into titles (title, link) values(?, ?)"
for title in titles:
    try:
        print(title)
        cur.execute(sql, title)
    except:
        pass
db.commit()
db.close()
print('Done!')