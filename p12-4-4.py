import requests, time
from bs4 import BeautifulSoup
url = "https://www.mobile01.com/topiclist.php?f=751"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")
pages = soup.find_all("a", class_="c-pagination")
last_page = int(pages[-1].text)
url_pattern = "https://www.mobile01.com/topiclist.php?f=751&p={}"
for page in range(1, last_page+1):
    current_url = url_pattern.format(page)
    html = requests.get(current_url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.find_all("div", class_="c-listTableTd__title")
    for title in titles:
        print(title.a.text)
        print(title.a['href'])
    time.sleep(3)    