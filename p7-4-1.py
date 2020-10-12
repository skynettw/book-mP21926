import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/77.0.3865.120 Safari/537.36'}
html=requests.get("https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020",headers=headers).text
from pprint import pprint
soup=BeautifulSoup(html,"html.parser")
sel = 'li.item'
ranking=soup.select(sel)
for no, book in enumerate(ranking, 1):
    print("第{}名".format(no))
    print(book.h4.a.text)
    detail = book.find_all("li")
    print(detail[0].text)
    print(detail[1].text)
    print("----")