# 數組（Tuple）、集合（Set）以及詞典（Dictionary），數組合併排序

L=[]
for i in range(2):
    print("Creat tuple%d:"%(i+1))
    while(True):
        n=eval(input())
        if n==-9999:break
        L.append(n)
T=tuple(L)
L.sort() #排序
print("Combined tuple before sorting:",T)
print("Combined list after sorting:",L)