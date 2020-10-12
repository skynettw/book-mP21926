import requests
url = "https://www.lexuscpo.com.tw/Home/CarStock"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
form_data = {
    "CarType":"", 
    "Series": "IS",
    "Price": "", 
    "Year": "", 
    "Mileage":"", 
    "StoreID":"", 
    "Page": "",
    "Limit": "20"
}
data = requests.post(url, data=form_data, headers=headers).text
print(data)

