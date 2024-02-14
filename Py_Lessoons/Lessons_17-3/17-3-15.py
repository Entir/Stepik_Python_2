def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as row:
        head = row.readline().rstrip().split(',')
        data = [item.split(',') for item in list(map(str.strip, row.readlines()))]
    result = []

    for i in data:
        x = dict()
        for j in range(len(i)):
            x[head[j]] = i[j]
        result.append(x)
    return result

print(read_csv())
