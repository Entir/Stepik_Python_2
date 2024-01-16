import random
length = int(input())
for _ in range(length):
    if random.randrange(2) == 1:
        print(chr(random.randrange(65, 91)), sep='', end='')
    else:
        print(chr(random.randrange(97, 123)), sep='', end='')