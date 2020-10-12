import requests
from bs4 import BeautifulSoup
url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")
pages = soup.find_all("a", class_="c-pagination")
print("本討論區的最後一頁是：", end="")
print(pages[-1].text)