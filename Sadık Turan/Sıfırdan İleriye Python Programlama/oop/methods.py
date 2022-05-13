from turtle import circle


class Circle:
    pi =3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    
    def cevre_hesapla(self):
        return 2*self.pi + self.yaricap

    def alan_hesapla(self):
        return self.pi * self.yaricap**2


circle1 = Circle(10)

print(circle1.alan_hesapla())
print(circle1.cevre_hesapla())