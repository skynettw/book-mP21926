import requests, json
from bs4 import BeautifulSoup

def send_simple_message(title, body):
    return requests.post(
        "https://api.mailgun.net/v3/drho.tw/messages",
        auth=("api", "key-558f8631d5fcc79a7ef85cafff3227e7"),
        data={"from": "PChome價格通知 <skynet.tw@gmail.com>",
              "to": ["minhuang@nkust.edu.tw"],
              "subject": title,
              "text": body })

url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc'
html = requests.get(url).text
products = json.loads(html)['prods']
message = ""
for product in products:
    if product['price'] > 20000:
        message = message + "NT$:{}, {}\n".format(product['price'], product['name'])
send_simple_message("Mac Mini價格通知", message)
print("Done")