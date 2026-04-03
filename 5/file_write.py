import random

hangle = list("가나다라마바사아자차카타파하")

with open("info.txt", "w", encoding="utf-8") as file:
    for i in range(1000):
        name = random.choice(hangle) + random.choice(hangle)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        
        file.write("{}, {}, {}\n".format(name, weight, height))