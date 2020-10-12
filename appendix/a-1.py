url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
import requests

html = requests.get(url).text
print(html)