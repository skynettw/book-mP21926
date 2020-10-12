import pprint as pp
import time, requests

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

for page in pages:
    html = requests.get(page).text
    pp.pprint(html)
    time.sleep(3)
    print("=========================")
