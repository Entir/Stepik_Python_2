import math


def execute_fun(num, fu):
    sample = {'квадрат': num**2,
              'куб': num**3,
              'корень': num**0.5,
              'модуль': abs(num),
              'синус': math.sin(num)
              }
    return sample[fu]


number = int(input())
fun = input()

print(execute_fun(number, fun))
