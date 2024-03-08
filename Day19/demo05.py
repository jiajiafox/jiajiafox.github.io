import openpyxl
fileName="README.xlsx"
wb=openpyxl.load_workbook(fileName)
s1=wb['Sheet']

s1['d1'].value='=sum(b1:c1)'
s1['d2'].value='=sum(b2:c2)'
s1['d3'].value='=sum(b3:c3)'
s1['d4'].value='=sum(b4:c4)'

wb.save(fileName)