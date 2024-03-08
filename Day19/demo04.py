from openpyxl import Workbook
import openpyxl
# 建立檔案
fileName="README.xlsx"
# wb=Workbook()   
# wb.save(fileName)

# 讀取
wb=openpyxl.load_workbook(fileName)

# 設定工作表
s1=wb['Sheet']

s1['A1'].value='java'
s1['A2'].value='python'
s1['A3'].value='php'
s1['A4'].value='C#'