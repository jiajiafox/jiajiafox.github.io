#導入model
import tkinter #QT

window=tkinter.Tk()
window.title("視窗作業")  #設定視窗title
window.geometry('480x340')  #設定視窗大小
window.configure(bg='#ADADAD') #設定背景顏色

# label表單，entry輸入框
login_label=tkinter.Label(window,text='登入系統',bg='#ffd2d2',fg='#272727') # fg= 字體顏色
login_label.grid(row=0,column=0,columnspan=2) #columnspan=X 跨X格

userName_label=tkinter.Label(window,text='帳號 :',bg='#00aeae',fg='#272727')
userName_label.grid(row=1,column=0)
userName_entry=tkinter.Entry(window)
userName_entry.grid(row=1,column=1)

passWord_label=tkinter.Label(window,text='密碼 :',bg='#00aeae',fg='#272727')
passWord_label.grid(row=2,column=0)
passWord_entry=tkinter.Entry(window,show='*')
passWord_entry.grid(row=2,column=1)

login_button=tkinter.Button(window,text='  登 入  ',bg='#ffbd9d',fg='#272727')
login_button.grid(row=3,column=0,columnspan=2)


window.mainloop()