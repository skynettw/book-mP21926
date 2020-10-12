from selenium import webdriver
from bs4 import BeautifulSoup
import time
url = 'https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID=menu'
web = webdriver.Chrome('chromedriver.exe')
web.implicitly_wait(60)
web.get(url)
html = web.page_source
web.quit()

