from selenium import webdriver
import pyautogui as auto
import pandas as pd
import time

url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
web = webdriver.Chrome("chromedriver.exe")
web.implicitly_wait(60)
web.get(url)
web.maximize_window()
auto.PAUSE = 3
auto.moveTo(1263, 438, 2)
auto.click()
auto.typewrite("2330")
auto.moveTo(1461, 438, 2)
auto.click()
time.sleep(5)
html = web.page_source
web.quit()
data = pd.read_html(html)
print(data)

