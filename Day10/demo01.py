def method(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":
        return a//b
    else:
        pass
a1=int(input("請輸入計算A值:"))
a2=int(input("請輸入計算B值:"))
a3=(input("請輸入四則運算符號:"))
count=method(a1,a2,a3)
print(count)