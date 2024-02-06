adress = input().split('.')

result = all(map(lambda x: True if x.isdigit() and (255 >= int(x) >= 0) else False, adress))

print(result)
