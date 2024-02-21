class School(object):
    def method(self):
        print("SCHOOL")

class Teacher(object):
    def method(self):
        print("TEACHER")

class Student(School,Teacher):  #多繼承(放在前面的會先運行=>school)
    pass

s=Student()
s.method()