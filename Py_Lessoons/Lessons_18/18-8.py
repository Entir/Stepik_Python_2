name = input()
with open(name, 'r', encoding='utf-8') as file:
    text = [i.rstrip() for i in file.readlines()]

result = []
for i in range(len(text)):
    if ('def' in text[i]) and ('#' not in text[i-1]):
        result.append(text[i])

if len(result) == 0:
    print('Best Programming Team')
else:
    for i in result:
        a = i[4:]
        x = a.find('(')
        print(a[:x])
