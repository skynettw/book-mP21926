import re
url = 'https://www.bagong.cn/dog/'

html = requests.get(url).text


regex = r'https?://.+.jpg'
photos = re.findall(regex, html)
for photo in photos:
    print(photo)
