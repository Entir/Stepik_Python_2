from fractions import Fraction, gcd

n = int(input())
result = []
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if i + j == n and i < j and gcd(i, j) == 1:
            result.append(Fraction(i, j))

print(max(result))
