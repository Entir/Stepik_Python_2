name = input()
with open(name, 'r', encoding='utf-8') as file:
    count = 0
    line = file.readline()
    while line != '':
        line = file.readline()
        count += 1

    if count <= 10:
        file.seek(0)
        print(*[i.rstrip() for i in file.readlines()], sep='\n')
    else:
        file.seek(0)
        result = []
        total = 0
        line = file.readline()
        while line != '':
            line = file.readline()
            total += 1
            if total >= count - 10:
                result.append(line.rstrip())
        print(*result, sep='\n', end='')

