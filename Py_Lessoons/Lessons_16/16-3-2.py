from functools import reduce
def product_of_odds(data):
    return reduce(lambda a, b: a * b, filter(lambda x: x if x % 2 == 1 else None, data), 1)


print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

