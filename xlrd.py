import xlrd as xlrd
book = xlrd.open_workbook("C:/Users/mdkaushar.nazir/Documents/d.xlsx")
sheet = book.sheet_by_index(1)

StringId="ID_00013"
Language="English - United Kingdom"

a=""
b=""


list_r = []
list_c = []
for k in range(0,sheet.nrows):
    list_r.append(sheet.row_values(k))
for k in range(0,sheet.ncols):
    list_c.append(sheet.col_values(k))

for index1 in range(len(list_c)):
    for index2 in range(len(list_c[index1])):
        if list_c[index1][index2]==Language:
            a=index1

for index1 in range(len(list_r)):
    for index2 in range(len(list_r[index1])):
        if list_r[index1][index2]==StringId:
            b=index1
print(list_r[b][a])


