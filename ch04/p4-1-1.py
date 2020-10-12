import requests
url = 'https://udn.com/news/breaknews/1/99#breaknews'

resp = requests.get(url)
html = resp.text
print(resp.status_code)
q = input("請輸入你要查詢的詞：")
while q != "":
    print(html.count(q))
    q = input("請輸入你要查詢的詞：")