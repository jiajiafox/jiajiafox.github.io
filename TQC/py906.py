# 檔案與異常處理，字串資料取代

fName=input()
s1=input()
s2=input()
with open(fName,"r+",encoding="UTF-8") as file:
    data=file.read()
    print("=== Before the replacement")
    print(data)
    print("=== After the replacement")
    data=data.replace(s1,s2)
    print(data)
    file.seek(0)
    file.write(data)