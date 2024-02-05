from functools import reduce


def evaluate(coefficients, x):
    i_c = [i for i in range(len(coefficients))]
    result = reduce(lambda aa, bb: aa + bb, map(lambda a, b: int(a) * x ** b, coefficients, i_c[::-1]))
    return result


c = input().split()
a = int(input())
print(evaluate(c, a))
