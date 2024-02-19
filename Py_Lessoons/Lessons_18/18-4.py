with open('words.txt', 'r', encoding='utf-8') as file:
    wrd = file.readline().split()

size = len(max(wrd, key=lambda w: len(w)))
result = list(filter(lambda w: len(w) >= size, wrd))
print(*result, sep='\n')
