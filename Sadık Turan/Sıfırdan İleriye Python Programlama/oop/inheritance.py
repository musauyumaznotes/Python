class Person():
    def __init__(self):
        print("Person Created")

class Student(Person):
    def __init__(self): 
        print("Student Created")

p1 = Person()
s1 = Student()