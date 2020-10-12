import requests
import os, csv
url = 'http://stats.moe.gov.tw/files/detail/108/108_student.csv'
csvdata = requests.get(url).text
rows = csvdata.split('\n')
data = list()
columns = rows[0].split(',')
for row in rows[1:]:
    try:
        row = row.split(',')
        item = list()
        for f_index in range(1, 5):
            item.append(row[f_index].replace('"', ''))
        data.append(item)
    except:
        pass
with open(os.path.basename(url), "w", encoding='utf-8', newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(columns[1:5])
    writer.writerows(data)
print("done")