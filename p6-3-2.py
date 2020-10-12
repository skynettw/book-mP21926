from selenium import webdriver
from bs4 import BeautifulSoup
import time
url = 'https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID=68'
web = webdriver.Chrome('chromedriver.exe')
web.implicitly_wait(60)
web.get(url)
html = web.page_source
time.sleep(10)
web.quit()

soup = BeautifulSoup(html, 'html.parser')
sel = '#stations > tr'
rows = soup.select(sel)
data = list()
for row in rows:
    try:
        header = row.find_all('th')
        fields = row.find_all('td')
        current_time = fields[0].text
        data.append((header[0].a.text.strip(), float(fields[1].text), int(fields[7].text)))
    except:
        pass
print("資料查詢時間", current_time)
print(data)