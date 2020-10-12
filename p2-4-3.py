import pprint as pp
import xlrd
filename = "scores.xlsx"

data = xlrd.open_workbook(filename)
sheets = data.sheets()

scores = dict()
for sheet in sheets:
    rows = list()
    for i in range(sheet.nrows):
        row = dict()
        if i == 0:
            columns = sheet.row_values(i)
        else:
            for f, field in enumerate(sheet.row_values(i)):
                row[columns[f]] = field
            rows.append(row)
    scores[sheet.name] = rows
pp.pprint(scores)