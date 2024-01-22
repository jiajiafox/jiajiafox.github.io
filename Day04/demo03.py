name=input("請輸入帳號:")
passw=input("請輸入密碼:")

#len()計算字數

if len(name)==0 or len(passw)==0:
    print("請輸入帳號密碼!!!")
else:
    if name=="fox" and passw=="123":
        print("歡迎登入")
    else : print("帳號或密碼輸入錯誤!!!")
