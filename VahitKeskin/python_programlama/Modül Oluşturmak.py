# Modul Olusturmak

#Hatalar / istisnalar (exceptions)

#ZeroDivisionError
a = 10
b = 0

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sifir olmaz")


#TypeError

a = 10
b = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Sayi ve string problemi")
    
    


a = 10
b = 2

a / b

try:
    print(a/b)
except TypeError:
    print("Sayi ve string problemi")