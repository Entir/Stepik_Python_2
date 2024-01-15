from fractions import Fraction

a = input()
b = input()
aa = Fraction(a)
bb = Fraction(b)

print(a, '+', b, '=', aa + bb)
print(a, '-', b, '=', aa - bb)
print(a, '*', b, '=', aa * bb)
print(a, '/', b, '=', aa / bb)
