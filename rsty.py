import xlrd,xlwt

from xlutils.copy import copy

book_to_make_copy=xlrd.open_workbook("xlrd.xls")

book_to_update=copy(book_to_make_copy)

sheet=book_to_update.get_sheet(0)
a=0
b=3
data=a*b
for i in range(5):
    for j in range(4):
        g=raw_input("enter the data.:")
        sheet.write(i,j,g)
book_to_update.save("xlrd.xls")       
        

