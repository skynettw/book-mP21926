from urllib import request
import json
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'
with request.urlopen(url) as res:
    data = json.loads(res.read().decode())
print(data[0])
