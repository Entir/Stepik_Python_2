order = {}
for _ in range(int(input())):
    user, item, q = input().split()
    if user not in order:
        order[user] = {item: int(q)}
    elif item not in order[user]:
        order[user][item] = int(q)
    else:
        order[user][item] = order[user].get(item, 0) + int(q)

for i in sorted(order.keys()):
    print(f'{i}:')
    for j in sorted(order[i]):
        print(j, order[i][j])
