k=eval(input())
for i in range(k):
    s=input()
    L=[eval(i) for i in s.split()]
    print("%.2f" %(max(L)-min(L)))