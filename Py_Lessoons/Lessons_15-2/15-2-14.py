def print_products(*args):
    prod = []
    for i in args:
        if type(i) is str and len(i) > 0:
            prod.append(i)
    if len(prod) == 0:
        print('Нет продуктов')
    else:
        for i in range(len(prod)):
            print(f'{i+1}) {prod[i]}')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)

