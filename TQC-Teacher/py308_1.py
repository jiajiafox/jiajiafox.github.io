n=eval(input())
for i in range(n):
    s=input()
    L=[int(j) for j in s]
    print("Sum of all digits of %s is %s" %(s,sum(L)))