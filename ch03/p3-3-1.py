import csv
import requests

url = 'http://stats.moe.gov.tw/files/detail/{}/{}_student.csv'
for year in range(103, 109):
    print(url.format(year, year))
