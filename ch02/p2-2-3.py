import pprint as pp
import csv
filename = 'info.csv'
data = list()
with open(filename, 'rt') as fp:
    rows = csv.DictReader(fp)
    print(type(rows))
    for row in rows:
        data.append(dict(row))
pp.pprint(data)