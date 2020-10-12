import requests
import csv
url = 'http://stats.moe.gov.tw/files/detail/108/108_student.csv'
data = list()
csvdata = requests.get(url).text
rows = csvdata.split('\n')
print(rows[0])