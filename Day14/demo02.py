# 類方法

class Cat(object):
    #類屬性
    tooth1=100

    #私有化屬性
    __tooth=10
    @classmethod
    def method(cls):
        print("類方法")
        print(cls.__tooth)
        print(cls.tooth1)

    def myMethod(self):
        print("一般方法")
        print(self.__tooth)
        print(self.tooth1)

c=Cat()
c.method()
c.myMethod()