import requests
from bs4 import BeautifulSoup

url = 'https://www.nkust.edu.tw/p/403-1000-12-1.php'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')
for link in links:
    print(link)