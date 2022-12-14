# Yan Etkisiz Fonksiyonlar (Pure Functions)

# Ornek1:Bagimsizlik

import numpy as np
A = 9


def impure_sum(b):
    return b + A


def pure_sum(a, b):
    return a+b


impure_sum(6)
pure_sum(3, 4)

# Ornek2:Olumcul Yan Etkiler
# OOP


class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)


lc = LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

# Functional Programming


def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]


def count(lines):
    return len(lines)


example_lines = read("deneme.txt")
lines_count = count(example_lines)
lines_count


# İsimsiz Fonksiyonlar (Anonymous Functions)

def old_sum(a, b):
    return a+b


old_sum(4, 5)


def new_sum(a, b): return a+b


new_sum(4, 5)


sirasiz_liste = [('b', 3), ('a', 8), ('d', 12), ('c', 1)]
sirasiz_liste

sorted(sirasiz_liste, key=lambda x: x[1])


# Vektörel Operasyonlar
# OOP
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

ab

# Functional Programming
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a*b

# Map & filter & reduce

liste = [1, 2, 3, 4, 5]

for i in liste:
    print(i+10)

list(map(lambda x:x*10 , liste))


#filter
liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x : x% 2 == 0,liste))


#reduce

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b:a+b,liste)








































