import json

data = [
    {'姓名':'王小明', '身高':174, '體重':56},
    {'姓名':'林小華', '身高':185, '體重':80},
    {'姓名':'陳小強', '身高':168, '體重':60} ]

with open('p-data.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp)
print("done")
        