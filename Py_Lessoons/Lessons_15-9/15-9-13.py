password = input()

result = (any(map(lambda x: True if x.islower() else False, password))
          + any(map(lambda x: True if x.isupper() else False, password))
          + any(map(lambda x: True if x.isdigit() else False, password)))

print('YES' if result == 3 and len(password) >= 7 else 'NO')
