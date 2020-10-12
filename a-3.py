from selenium import webdriver
url = "c:\\users\\skyne\\a-2.html"
web = webdriver.Chrome("chromedriver.exe")
web.get(url)
print(web.page_source)
