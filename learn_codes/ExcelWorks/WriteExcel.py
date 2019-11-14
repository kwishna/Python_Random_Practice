# import xlwt
#
# wb = xlwt.Workbook()
# sheet2 = wb.add_sheet('WritingThroughPython', True)
# for i in range(5):
#     for j in range(5):
#         sheet2.write(i, j, 'Krishna'+str(i)+str(j))
#
# wb.save('ExcelWrite.xls')

##########################################################################

# import openpyxl
#
# wb1 = openpyxl.Workbook()
# xsheet = wb1.create_sheet('Sheet', 0)
# for i in range(1, 5):
#     for j in range(1, 5):
#         xcell = xsheet.cell(i, j)
#         xcell.value = 'Krishna'+str(i)+str(j)
#
# wb1.save('ExcelByOpenPyxL.xlsx')


