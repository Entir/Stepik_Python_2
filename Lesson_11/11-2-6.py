access = {'write': 'W', 'read': 'R', 'execute': 'X'}
file = {}

for i in range(int(input())):
    a = input().split()
    file[a[0]] = a[1:]

for i in range(int(input())):
    b = input().split()
    if access[b[0]] in file[b[1]]:
        print('OK')
    else:
        print('Access denied')
