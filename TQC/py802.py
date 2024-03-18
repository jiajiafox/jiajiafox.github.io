# 字串(String)的運作，字元對應

s=input()
sum=0
for i in range(len(s)):
    print("ASCII code for '%s' is %d" %(s[i],ord(s[i])))
    sum+=ord(s[i])
print(sum)