class MyClass1(object):

    #變數(放置於 def，就是變數(區域變數))
    #初始化 def
    #放在 def 外， class 內 屬性(全域變數，)
    x=0
    def __init__(self):     #用來初始化參數(預設值/數值)，調用class就會載入(與claa綁定)
        self.code="python"  #預設的值(def內部)
        self.age=25
        
    def __str__(self):
        return f"{self.code}{self.age}"

    # def __del__():

    def myDef(self):
        print(f"{self.code}{self.age}")


f=MyClass1
print(f)