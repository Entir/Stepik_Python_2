import random

nums = [str(i) for i in range(1, 76)]
random.shuffle(nums)
count = 0
bingo = [[] for i in range(5)]

for i in range(5):
    for j in range(5):
        bingo[i].append(nums[count])
        count += 1
bingo[2][2] = 0

for item in bingo:
    for j in item:
        print(str(j).ljust(3), end='')
    print()
