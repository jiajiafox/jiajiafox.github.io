class A():
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
class C():
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
a=A("Stanley")  #輸入回傳值
print(a)
c=C("Debby")    #輸入回傳值
print(c)