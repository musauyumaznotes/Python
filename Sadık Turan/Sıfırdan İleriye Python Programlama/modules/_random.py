import random
from unicodedata import name

# result = dir(random)
# result = help(random)

result = random.random()
result = random.random() * 100
result = random.uniform(10,100)
result = random.randint(1,100)

greeting = "hello there"
names = ["ali","Yağmur","deniz","cenk","ahmet","cenk"]
# result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))

result = liste
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste,3)
result = random.sample(names,2)

print(result)
