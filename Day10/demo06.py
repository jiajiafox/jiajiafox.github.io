# *args : 可變參數，可無限傳入，表現形式為元祖()。
# **kargs : 

def method(*args):
    return args
x=method(10,20,30,40,50,60,70,80,90,100)
print(x)


fun1=lambda *args:args
print(fun1(10,20,30,40,50,60,70,80,90,100))