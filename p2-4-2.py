import xlrd
filename = "scores.xlsx"

data = xlrd.open_workbook(filename)
s1 = data.sheets()[0]
for row in range(s1.nrows):
    print(s1.row_values(row))