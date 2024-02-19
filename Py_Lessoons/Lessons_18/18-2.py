with open('ledger.txt', 'r', encoding='utf-8') as file:
    result = [int(x.lstrip('$')) for x in [i.rstrip() for i in file.readlines()]]

print('$', sum(result), sep='')
