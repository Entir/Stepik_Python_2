name = input()
with open(name, 'r', encoding='utf-8') as file:
    result = len(file.readlines())
print(result)
