import requests, json
url = "https://www.lexuscpo.com.tw/Home/CarStock"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
form_data = {
    "CarType":"", 
    "Series": "",
    "Price": "", 
    "Year": "", 
    "Mileage":"", 
    "StoreID":"", 
    "Page": "",
    "Limit": "500"
}
data = requests.post(url, data=form_data, headers=headers).text
cars = json.loads(data)
cars = cars['rows']
message = "{:<10}({}年式)，{:>10,}KM，{:>10,}元"
for car in cars:
    print(message.format(
        car['Model'], 
        car['Year'],
        car['Mileage'],
        car['SellPrice']))

