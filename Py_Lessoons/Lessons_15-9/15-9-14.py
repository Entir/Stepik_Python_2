point = []
for i in range(int(input())):
    point.append(any(map(lambda x: True if int(x[1]) > 4 else False, [input().split() for _ in range(int(input()))])))
print('YES' if all(point) else 'NO')
