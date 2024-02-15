import random


with open('random.txt', 'w', encoding='utf-8') as file:
    for i in range(25):
        print(random.choice(range(111, 778)))

