class A():
    def method(self):   #父類別空白，子類別繼承，覆寫(業界、公司常用)
        pass

class C():
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    

c=C("Debby")    #輸入回傳值
print(c)