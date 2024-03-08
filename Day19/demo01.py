# 建立 Excel

from openpyxl import Workbook
from openpyxl import load_workbook

fileName="1.xlsx"
wb=Workbook()
wb.save(fileName)
# ws=wb.active
# ws.title="aaa"