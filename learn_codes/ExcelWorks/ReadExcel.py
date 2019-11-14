# import xlrd
#
# book = xlrd.open_workbook('ExcelRead.xlsx')
# sheet = book.sheet_by_name('Sheet1')
#
# rowsNo = sheet.nrows
# colsNo = sheet.ncols
#
# for i in range(rowsNo):
#     print()
#     for j in range(colsNo):
#         val = sheet.cell_value(i, j)
#         print(val, end='  |  ')

##########################################################################

# import openpyxl
#
# wb = openpyxl.load_workbook('ExcelRead.xlsx')
# print(wb.sheetnames)
#
# sheet = wb['Sheet1']
# rowsCount = sheet.max_row
# colsCount = sheet.max_column
#
# for i in range(1, rowsCount+1):
#     print()
#     for j in range(1, colsCount+1):
#         cell = sheet.cell(i, j)
#         print(cell.value, end='  |  ')