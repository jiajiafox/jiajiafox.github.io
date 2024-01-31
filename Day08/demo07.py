str1=" you are IDIOT idIot "
s1=str1.lower()  #全改小寫
print(s1)
s2=s1.replace("idiot","****")   # 改字(old,new,改的次數)
print(s2) 

str2="you,are,idIot"
print(str2.split(","))