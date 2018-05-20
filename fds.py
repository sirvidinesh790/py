"""
import xlrd
exbook=xlrd.open_workbook("a.xlsx")

sheet=exbook.sheet_by_index(0)
total_row=sheet.nrows
total_cols=sheet.ncols
for i in range(4):
    for j in range(2):
        cell_value=sheet.cell(i,j).value
        print cell_value
        print ""
"""        
import xlwt
wb=xlwt.workbook()
sh=wb.add_sheet("sheet.1")

sh.write(0,0,"data")
wb.save("b.xlsx")
