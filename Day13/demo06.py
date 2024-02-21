class A(object):
    def __init__(self):
        print("__init__")

    def method(self):
        print("aaa")

class C(A):
    def getMethod(self):
        super().__init__()  #super 呼叫父類別class
        super().method()
        

class B(A):
    def make(self):
        A.__init__(self)
        A.method(self)

b=B()
b.make()