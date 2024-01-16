import random
n = int(input())
for _ in range(n):
    drop = random.randrange(2)
    print('Орел' if drop == 1 else 'Решка')

