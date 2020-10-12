import pprint as pp
import csv
filename = 'info.csv'
with open(filename, 'rt') as fp:
    rows = csv.DictReader(fp)
    data = [dict(row) for row in rows]
pp.pprint(data)