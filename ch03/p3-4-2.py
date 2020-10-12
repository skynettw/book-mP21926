from urllib import request
import json, csv
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'
with request.urlopen(url) as res:
    products = json.loads(res.read().decode())
print('products.csv is writing...')
with open('products.csv', 'w', encoding ='UTF-8', newline = '\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(('作物名稱','平均價','交易量'))
    for item in products:
        writer.writerow((item['作物名稱'],item['平均價'],item['交易量']))
print('done')
