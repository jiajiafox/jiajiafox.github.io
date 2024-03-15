# 進階控制流程，繪製等腰三角形

n=eval(input())
for i in range(n):
    for j in range(n-i-1):print(" ",end="")
    for k in range(2*i+1):print("*",end="")
    print("")