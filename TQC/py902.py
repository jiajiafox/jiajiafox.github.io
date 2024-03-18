# 檔案與異常處理，資料加總

f=open("read.txt","r",encoding="UTF-8")
data=f.read()
L=[int(i) for i in data.split()]
print(sum(L))
f.close(L)