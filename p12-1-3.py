from selenium import webdriver
import pyautogui as auto
import pandas as pd
import time

stocks = [
    {
        "name": "聯電",
        "id": "2303"
    },
    {
        "name": "台積電",
        "id": "2330"
    },
    {
        "name": "華碩",
        "id": "2357"
    }
]

url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
web = webdriver.Chrome("chromedriver.exe")
web.implicitly_wait(60)
web.get(url)
web.maximize_window()
auto.PAUSE = 3
for stock in stocks:
    auto.moveTo(1263, 438, 2)
    auto.doubleClick()
    auto.typewrite(stock["id"])
    auto.moveTo(1461, 438, 2)
    auto.click()
    time.sleep(5)
    html = web.page_source
    data = pd.read_html(html)
    print(stock["name"])
    print(data[0])
web.quit()

