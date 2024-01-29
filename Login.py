#導入model
import tkinter #QT
from tkinter import messagebox

window=tkinter.Tk()
window.title("視窗作業")         #設定視窗title。
window.geometry('340x340')      #設定視窗大小。
window.configure(bg='#FFF8D7')  #設定視窗背景顏色。

#函數 function  方法 mothod
def login():
    username="fox"
    PassWord="123"
    entry_name=userName_entry.get()
    entry_pass=passWord_entry.get()
    if len(entry_name)>0 and len(entry_pass)>0:
        if entry_name==username and entry_pass==PassWord:
            messagebox.showinfo(title="登入頁面",message=f"歡迎{userName_entry.get()}登入系統")
        else:
            messagebox.showinfo(title="登入失敗",message="帳號或密碼輸入錯誤")
    else:
         messagebox.showinfo(title="登入錯誤",message="請輸入帳號密碼")  

frame=tkinter.Frame(bg='#FFF8D7',pady=25)

# 添加標籤元素(label表單，entry輸入框)
login_label=tkinter.Label(frame,text='員工登入系統',bg='#FFF8D7',fg='#000000',font=('Arial',24)) 
# fg= 字體顏色 ，font=(('x字型',x))字體樣式、大小。
login_label.grid(row=0,column=0,columnspan=2,sticky='news',pady=25)   #columnspan=X 跨X格

userName_label=tkinter.Label(frame,text='員工帳號 :',bg='#FFF8D7',fg='#000000',font=('Arial',12))
userName_label.grid(row=1,column=0)
userName_entry=tkinter.Entry(frame,font=('Arial',12))
userName_entry.grid(row=1,column=1,pady=15)

passWord_label=tkinter.Label(frame,text='員工密碼 :',bg='#FFF8D7',fg='#000000',font=('Arial',12))
passWord_label.grid(row=2,column=0)
passWord_entry=tkinter.Entry(frame,show='*',font=('Arial',12))
passWord_entry.grid(row=2,column=1,pady=15)

login_button=tkinter.Button(frame,text='  登 入  ',bg='#003E3E',fg='#ffffff',command=login)
login_button.grid(row=3,column=0,columnspan=2,pady=20)

frame.pack()

# 啟動事件循環
window.mainloop()