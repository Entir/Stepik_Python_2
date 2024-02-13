with open('data.txt', 'r', encoding='utf-8') as file:
    txt = [line.rstrip() for line in file.readlines()]
print(*txt[::-1], sep='\n')
