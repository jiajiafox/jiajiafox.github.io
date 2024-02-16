f=open("cc.txt","r+",encoding='UTF-8')
con=f.read()
#seek(偏移量，起始位置) 指針位置
#0開頭，1當前，2結尾
f.seek(1,0)
print(con)
f.close() 