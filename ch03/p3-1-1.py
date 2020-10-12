import pprint as pp
url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 18):
    pages.append(url.format(pg))
pp.pprint(pages)
