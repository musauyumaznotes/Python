# def square(num):return num**2
square =lambda num: num**2
numbers = [1,3,5,9]
result=list(map(square,numbers))

#result =square(2)
print(result)