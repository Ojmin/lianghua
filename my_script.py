import pandas as pds
import numpy as np
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
import xlwt

data = xlrd.open_workbook("aa.xlsx")
my_data = []
table = data.sheets()[4]
for i in range(1, 3000):
    try:
        for j in range(2, 500):
            try:
                premium_rt = table.row_values(i)[j]
                if premium_rt < -0.5:
                    date = datetime(*xldate_as_tuple(table.row_values(i)[0], 0))
                    cell = date.strftime('%Y-%m-%d')
                    my_data.append(
                        [cell, table.col_values(j)[0],
                         table.col_values(j)[1], premium_rt])
            except:
                print(  "gg")
    except:
        print("ff")
f = xlwt.Workbook()
sheet = f.add_sheet("bond", cell_overwrite_ok=True)
row0 = [u'日期', u'代码', u'名称', u'溢价率']
for i in range(0, len(row0)):
    sheet.write(0, i, row0[i])
k = 0
for j in my_data:
    k += 1
    for i in range(0, len(j)):
        sheet.write(k, i, j[i])
f.save("ccc.xls")
