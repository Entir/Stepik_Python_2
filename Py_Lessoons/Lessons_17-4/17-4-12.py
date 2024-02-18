with open('goats.txt', 'r', encoding='utf-8') as file:
    line = ''
    while line != 'GOATS\n':
        line = file.readline()

    total = sorted([i.rstrip() for i in file.readlines()])

c_goat = {}
for item in total:
    if c_goat.get(item, None):
        c_goat[item] += 1
    else:
        c_goat[item] = 1

with open('answer.txt', 'w', encoding='utf-8') as out_file:
    for key in c_goat:
        if c_goat[key] / len(total) > 0.07:
            print(key, file=out_file)
