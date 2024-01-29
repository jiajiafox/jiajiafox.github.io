age=int(input("請輸入年紀 :"))
if age>0 and age<=120:
    if age>4 and age<=6:
        print("幼幼")
    elif age>6 and age<=10:
        print("小小")
    else:
        pass
else:
    print("你是人類嗎?")