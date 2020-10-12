import requests
url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"
data = requests.get(url).text
print(data)
