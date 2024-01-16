from decimal import *
num = Decimal(input())

result = num.as_tuple()

if abs(num) > 1:
    print(min(result.digits) + max(result.digits))
else:
    print(max(result.digits))
