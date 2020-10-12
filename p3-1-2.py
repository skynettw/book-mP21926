import pprint as pp
import requests
url = "https://www.nkust.edu.tw/p/403-1000-14-1.php?Lang=zh-tw"

html = requests.get(url).text
pp.pprint(html)