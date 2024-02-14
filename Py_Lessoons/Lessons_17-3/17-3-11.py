with open('nums.txt', 'r', encoding='utf-8') as f:
    raw = f.readlines()

total = ''

for i in raw:
    for j in i:
        if j.isdigit():
            total += j
        else:
            total += ' '
result = sum(map(lambda x: int(x), total.split()))
print(result)
