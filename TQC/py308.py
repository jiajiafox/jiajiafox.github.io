# 迴圈敘述，迴圈位數加總

n=eval(input())
for i in range(n):
    tmp=num=eval(input())
    sum=0
    while(tmp>0):
        sum+=tmp%10
        tmp=tmp//10
        print("Sum of all digits of %d is %d" %(num,sum))