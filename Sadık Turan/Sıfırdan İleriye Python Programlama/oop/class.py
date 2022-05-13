#class

#object , instance

class Person:
    # pass
    def __init__(self,name,year):
        self.name = name
        self.birthYear = year
        print("init metodu çalıştı")
    #attributes
    #methods

p1 = Person("Musa",1999)
print(f"p1 name: {p1.name} birthyear: {p1.birthYear}")
print(p1)
print(type(p1))
