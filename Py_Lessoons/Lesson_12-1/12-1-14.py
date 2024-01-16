import random
nums = set()
while len(nums) < 7:
    nums.add(random.randrange(1, 50))
print(*sorted(nums))

# 123123