# 寫 write
# 'w'的模組一定要寫，因為寫會需要檔案權限
o=open("cc.txt",'w')
o.write("haha") #更改寫的內容會覆蓋之前的內容
o.close() #關
