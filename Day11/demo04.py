# 文件(打開，關閉，讀，寫，複製，建立)
# 打開 open(name.mode) 讀 "r" 的模組可以省略
f=open("Day11/bb.txt")
c=f.read()      #讀
# c=f.readline()  #讀一行
# c=f.readlines()   #讀取所有的文字與程式碼
print(c)
f.close()