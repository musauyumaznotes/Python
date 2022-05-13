def greeting(name):
    print("Hello" , name)

greeting("musa")

sayHello = greeting


def outer(num1):
    def inner_increment(num1):
        return num1+1