n = int(input())
z1 = complex(input())
z2 = complex(input())

result = (z1 ** n) + (z2 ** n) + (z1.conjugate() ** n) + (z2.conjugate() ** (n+1))

print(result)
