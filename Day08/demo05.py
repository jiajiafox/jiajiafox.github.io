#程式顯示以字串表示:"",'',""""""
str1="beautiful fin" 
str2='beautiful fin'
str3="""beautiful fin"""
print(len(str1))

#索引值(0為起始值)
print(str1[2:5:1])  # [開始位置的索引:結束位置的索引:長度]
print(str1[:5])     # :索引值前 (beaut)
print(str1[5:])     # 索引值後: (iful fin)
t=str1.find('ful',2,10)
print(t)
print(str1[6])
print(str1.index('ful'))

x=str1.count('i')
print(x)