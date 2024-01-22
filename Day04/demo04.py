name=input("請輸入帳號:")
passw=input("請輸入密碼:")


if len(name)!=0 or len(passw)!=0:
    if name=="fox" and passw=="123":
        print("歡迎登入")
    else : print("帳號或密碼輸入錯誤!!!")
else :
    print("請輸入帳號密碼!!!")

