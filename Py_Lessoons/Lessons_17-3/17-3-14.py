with open('population.txt', 'r', encoding='utf-8') as f:
    result = list(map(lambda i: i.split('\t'), list(map(str.strip, f.readlines()))))

total = [item[0] for item in result if item[0][0] == 'G' and int(item[1]) > 500000]

print(*total, sep='\n')
