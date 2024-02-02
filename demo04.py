dic={"name":"stanley","age":26}
dic1={"name":"debby","age":25}
print(dic)

dic["gender"]="male"    #新增一個數據
dic["age"]=18   #修改原有數據
print(dic)
print(dic.keys())
print(dic.values())

del dic["age"]  #刪除
print(dic)

dic.clear() #清空
print(dic)

print(dic.items())