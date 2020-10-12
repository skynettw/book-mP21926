import requests
import re
url = 'https://www.taichung.gov.tw/10179/12034/'

html = requests.get(url).text

regex04a = r'\(\d{2}\)\d{4}-?\d{4}'
regex04b = r'\d{2}-\d{4}-?\d{4}'
regex0800 = r'0800-\d{6}'
matches = re.findall(regex04a, html)
matches += re.findall(regex04b, html)
matches += re.findall(regex0800, html)
for match in matches:
    print(match)
print(matches)