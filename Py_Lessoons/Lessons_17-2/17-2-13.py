import random


file = open('lines.txt')
txt = [line.rstrip() for line in file]
file.close()
print(random.choice(txt))
