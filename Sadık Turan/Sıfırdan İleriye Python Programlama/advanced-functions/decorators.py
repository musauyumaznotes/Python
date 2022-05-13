def my_decorator(func):
    def wrapper():
        print("Fonksiyondan önceki işlemler")
        func()
        print("Fonksiyondan sonraki işlemler")
    return wrapper()

@my_decorator
def sayHello():
    print("hello")
# def sayGreeting():
#     print("greeting")


sayHello()