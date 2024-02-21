class X():

    def __init__(self):
        self.__name="S"

    def method(self):
        print("method")

    def __method1(self):
        self.__method1()  #私有化屬性，不給調用
        print("method1")

class T(X):
    def other(self):
       super().method()
       super().__method1()

x=X()
x.__method1()


t=T()
# t.__method1()
t.method()