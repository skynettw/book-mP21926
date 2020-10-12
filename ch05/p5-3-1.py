import requests
from bs4 import BeautifulSoup
url = 'https://newcar.u-car.com.tw/newcar'
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
makes = soup.select('#makeselect > option')
makers = dict()
for make in makes:
    if make['value'] != '0':
        makers[int(make['value'])] = make.text
print(makers)