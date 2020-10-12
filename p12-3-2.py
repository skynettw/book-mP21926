import json
import urllib.parse
import requests
url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"
html = requests.get(url).text
data = json.loads(html)
titles = data['lists']
for title in titles:
    print(title['title'])
    print(urllib.parse.urljoin("https://udn.com", title['titleLink']))