with open('numbers.txt', 'r', encoding='utf-8') as file:
    result = [line.rstrip().split() for line in file]

for i in range(len(result)):
    total = sum(map(lambda x: int(x), result[i]))
    print(total)
