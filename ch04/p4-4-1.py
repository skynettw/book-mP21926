import requests
from bs4 import BeautifulSoup

url = 'https://autos.udn.com/autos/story/9060/2187994'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all("a")
for link in links:
    try:
        if ".jpg" in link['href']:
            print(link['href'])
    except:
        pass