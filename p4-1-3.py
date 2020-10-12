import requests
import re
url = 'https://kknews.cc/zh-tw/home/kx5p5v8.html'

html = requests.get(url).text

regex = r'https?://.+.jpg'
photos = re.findall(regex, html)
for photo in photos:
    print(photo)