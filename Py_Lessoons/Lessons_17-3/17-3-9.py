with open('lines.txt', 'r', encoding='utf-8') as file:
    txt = [line.rstrip() for line in file.readlines()]

size = len(max(txt, key=lambda i: len(i)))
print(*[item for item in txt if len(item) == size], sep='\n')
