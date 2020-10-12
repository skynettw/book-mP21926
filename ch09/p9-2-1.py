import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "key-558f*******3227e7"),
        data={"from": "Excited User <skynet.tw@gmail.com>",
              "to": ["minhuang@nkust.edu.tw"],
              "subject": "Test mail from mailgun",
              "text": "這是一個測試郵件"})

send_simple_message()