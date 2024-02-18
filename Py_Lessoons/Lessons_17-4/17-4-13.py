names = [input() for _ in range(int(input()))]

with open('output.txt', 'w', encoding='utf') as out_file:
    result = []

    for name in names:
        with open(name, 'r', encoding='utf-8') as file:
            for item in file.readlines():
                result.append(item)

    out_file.writelines(result)
