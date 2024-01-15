from fractions import Fraction


n = int(input())
nums = set()

for i in range(1, n):
    for j in range(1, n+1):
        if i < j:
            nums.add(Fraction(i, j))

print(*sorted(nums), sep='\n')
