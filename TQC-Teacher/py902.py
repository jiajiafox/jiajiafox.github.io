f=open("read.txt","r",encoding="UTF-8")
data=f.read()
L=[int(i) for i in data.split()]
print(sum(L))
f.close()