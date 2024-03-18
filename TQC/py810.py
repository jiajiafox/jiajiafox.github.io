# 字串(String)的運作，最大值與最小值之差

k=eval(input())
for i in range(k):
    s=input()
    L=[eval(i) for i in s.split()]
    print("%.2f"%(max(L)-min(L)))