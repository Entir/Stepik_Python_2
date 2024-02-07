def pretty_print(data: list, side='-', delimiter='|'):
    midle = (delimiter).join([' ' + str(i) + ' ' for i in data])
    print(' ' + side * len(midle) + ' ')
    print(delimiter + midle + delimiter)
    print(' ' + side * len(midle) + ' ')




pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')