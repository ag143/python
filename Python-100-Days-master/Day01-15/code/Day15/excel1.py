"""
Create Excel file

Version: 0.1
Author: author
Date: 2018-03-26
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
     [1001, 'Bai Yuanfang', 'Male', '13123456789'],
     [1002, 'Bai Jie', 'Female', '13233445566']
]
sheet.append(['student number', 'name', 'gender', 'phone'])
for row in data:
     sheet.append(row)
tab = Table(displayName="Table1", ref="A1:E5")

tab.tableStyleInfo = TableStyleInfo(
     name="TableStyleMedium9", showFirstColumn=False,
     showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
workbook.save('./res/student data of the whole class.xlsx')