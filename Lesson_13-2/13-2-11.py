from fractions import Fraction
import math
n = int(input())
result = 0
for i in range(1, n + 1):
    result += Fraction(1, math.factorial(i))

print(result)