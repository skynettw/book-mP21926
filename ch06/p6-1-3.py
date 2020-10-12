import requests
from bs4 import BeautifulSoup

url = 'https://rate.bot.com.tw/xrt/all/day'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
buyingrate = soup.select('table tr td[data-table=本行即期買入]')
for price in buyingrate:
    print(price.text.strip())
