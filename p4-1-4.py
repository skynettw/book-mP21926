import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+)"
url = 'http://localhost:8000/email.html'

html = requests.get(url, verify=False).text
    
emails = re.findall(regex, html)
for email in emails:
    print(email)
