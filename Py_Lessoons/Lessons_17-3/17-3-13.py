import random


with open('first_names.txt') as f, open('last_names.txt') as l:
    list_f_nane = list(map(str.strip, f.readlines()))
    list_l_nane = list(map(str.strip, l.readlines()))

for i in range(3):
    result = (random.choice(list_f_nane), random.choice(list_l_nane))
    print(*result)
