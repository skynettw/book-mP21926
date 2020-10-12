from bs4 import BeautifulSoup
import requests

url_pattern = "https://www.nuk.edu.tw/p/403-1000-83-{}.php?Lang=zh-tw"
url = url_pattern.format(1)
sel = "#Dyn_2_3 > div > section > div.mpgbar > nav > span"
html = requests.get(url).text
response = BeautifulSoup(html, "lxml")
res = response.select(sel)
pages = int(res[0].text[1:-1])
all_links = list()
for page in range(pages):
	all_links.append(url_pattern.format(page+1))
print(all_links)