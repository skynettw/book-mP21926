import requests
url = "https://ck101.com/forum-3590-1.html?ref=nav"
res = requests.get(url)
print(res)
print(res.text)
