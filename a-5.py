import urllib.parse
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo#').text
soup = BeautifulSoup(html, 'html.parser')
captcha_image = soup.find('img', id='pickimg')['src'] 
csrf_token = soup.find_all('input', type='hidden') 
image_url = urllib.parse.urljoin('https://www.mvdis.gov.tw/', captcha_image)
print(image_url)
captcha = input("請輸入驗證碼：")
headers = {
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    "Cookie":'DWRSESSIONID=qNiI6i9UPxr4DV2G7PrFV8pkahn; _ga=GA1.3.1352658715.1598224971; BSESSIONID1=D106D274717EDF2C4EFDD9D698E61581.tsb22; _gid=GA1.3.615895194.1598974412; JSESSIONID1=B71AEB3133E436EA9619A6F6F3CDA2EA.tsp12'
}
data = {
    'method': 'qryPickNo',
    'selDeptCode': "2",
    'selStationCode': "30",
    'selWindowNo': "01",
    'selCarType': "M",
    'selEnergyType': "C",
    'selPlateType': "F",
    'plateVer': "2",
    'validateStr': str(captcha),
    'queryType': 0,
    'queryNo': '*',
    'CSRFToken': str(csrf_token[2]['value']),
}
html = requests.post('https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo', data = data, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')
plate_numbers = soup.find_all('a','number')
for plate_number in plate_numbers:
    print(plate_number.text)