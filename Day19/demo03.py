from openpyxl import Workbook
import openpyxl

fileName="aaaa.xlsx"
wb=openpyxl.load_workbook(fileName) 
s1=wb['工作表1']
# s1=wb.active

for row in s1.values:
    for value in row:
        print(value)