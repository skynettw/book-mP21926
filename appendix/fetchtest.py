import requests
from bs4 import BeautifulSoup

url = 'https://www.nkust.edu.tw/'
sel = '#sm_div_cmb_1_15062 > div > div > section'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
target = soup.p
print(target)