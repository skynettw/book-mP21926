import requests
from bs4 import BeautifulSoup

url = 'https://www.nkust.edu.tw/p/403-1000-12-1.php'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all(class_='mtitle')
for link in links:
    title = link.find('a')
    print(title.text.strip())
    print(title['href'])
    