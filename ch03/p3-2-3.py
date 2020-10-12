import csv

data = [
    ['王小明', 174, 56],
    ['林小華', 185, 80],
    ['陳小強', 168, 60] ]

with open('p-data2.csv', 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(['姓名', '身高', '體重'])
    csvwriter.writerows(data)
print("done")
        