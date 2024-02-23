#類屬性

class Dog(object):
    tooth=10


class Dog1(Dog):
    def getVar():
        return super().tooth() 

dog1=Dog1()
dog1.getVar()


d1=Dog()
print(d1.tooth)
d2=Dog()
print(d2.tooth)