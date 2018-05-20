import xlrd,xlwt
from xlutils.copy import copy
book_to_make_copy=xlrd.open_workbook("xlrd.xls")
book_to_update=copy(book_to_make_copy)
sheet=book_to_update.get_sheet(0)
print dir(sheet)
sheet.nrows
sheet.ncols
i=sheet.nrows
j=sheet.ncols
for i in range (5):
    for j in range(4):
        cell_value=sheet.cell(i,j)
        sheet.write(i,j,"data")
        book_to_update.save("xlrd.xls")
        print cell_value
