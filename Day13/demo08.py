# 物件導向重點:封裝，繼承，多型(多態(多種型態))
#沒有繼承，就沒有型態
class Dog(object):
    def __init__():
        pass
    
    def work(self):
        print("旺旺!!")

class AnyDog(Dog):
    def work(self):
        print("看門")

class Person(object):
    def work_with_dog(self,dog):
        dog.work()

dog1=AnyDog() 

per=Person()
per.work_with_dog(dog1)