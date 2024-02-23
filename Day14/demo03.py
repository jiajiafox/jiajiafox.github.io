class AA(object):
    s=10000

    #不須使用self
    @staticmethod
    def hh():
        return 
    
    #通常使用類屬性或私有屬性才會使用
    @classmethod
    def vv(cls):
        return cls.s

    def a(self):
        a=100
        print(self.s)
        print(a)

    def b(self):
        b=200
        print(self.s)
        print(b)

class BB(AA):
    def getVar(self):
        print(self.s)

# a=AA()
# a.a()
# a.b()
b=BB()
b.a()
b.b()

