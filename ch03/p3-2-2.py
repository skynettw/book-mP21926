import csv

data = [
    ['姓名', '身高', '體重'],
    ['王小明', 174, 56],
    ['林小華', 185, 80],
    ['陳小強', 168, 60] ]

with open('p-data.csv', 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerows(data)
print("done")
        