import requests
url = "https://www.mobile01.com/topiclist.php?f=751"
res = requests.get(url)
print(res)