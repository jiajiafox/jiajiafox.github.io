L=[]
for i in range(2):
    print("Create tuple%d:" %(i+1))
    while(True):
        n=eval(input())
        if n==-9999:break
        L.append(n)
T=tuple(L)
L.sort()
print("Combined tuple before sorting:",T)
print("Combined list after sorting:",L)