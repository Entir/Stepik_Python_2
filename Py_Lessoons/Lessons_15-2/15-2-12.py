def mean(*args):
    summ = 0.0
    count = 0
    for i in args:
        if type(i) is float or type(i) is int:
            count += 1
            summ += i
    if summ == 0:
        return 0.0
    return summ / count


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
