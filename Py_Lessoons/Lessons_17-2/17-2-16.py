file = open('prices.txt', encoding='utf-8')
order = []
for line in file:
    order.append(line.strip().split('\t'))
file.close()
print(sum([int(order[i][1]) * int(order[i][2]) for i in range(len(order))]))
