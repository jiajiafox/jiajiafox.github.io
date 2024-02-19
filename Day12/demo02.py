# class 類別，物件(實體)
class MyClass():    #建立一個class類別(大駝峰命名法)
    def getInt(self):   #self(this 其他程式的語法)，表示在這個class裡面
        print("def 01")
    
    def getFloat(self,x=20):    # x=? 給一個預設值
        print("def 02")

    def getString(self):
        return 200
    
    def getTuple(self,x,y):
        return x+y
    

t1=MyClass()        #建立實體(同個class可建立多個實體)
t1.getInt()
t1.getFloat()
d=t1.getString()
print(d)
j=t1.getTuple(100,200)
print(j)
t2=MyClass()
t3=MyClass()
t4=MyClass()