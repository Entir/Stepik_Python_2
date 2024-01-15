from fractions import Fraction

num = int(input())

result = 0
for i in range(1, num + 1):
    result += Fraction(1, i ** 2)

print(result)