import json, time
import urllib.parse
import requests
url_pattern = "https://udn.com/api/more?page={}&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"
alldata = list()
for page in range(1, 11):
    url = url_pattern.format(page)
    html = requests.get(url).text
    data = json.loads(html)
    titles = data['lists']
    for title in titles:
        item = dict()
        print(title['title'])
        item['title'] = title['title']
        item['url'] = urllib.parse.urljoin("https://udn.com", title['titleLink'])
        alldata.append(item)
    time.sleep(3)
with open("allnews.json", "w") as fp:
    json.dump(alldata, fp)
print("下載完畢！")