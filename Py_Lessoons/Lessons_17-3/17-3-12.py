with open('file.txt', 'r', encoding='utf-8') as f:
    count_lines = f.readlines()
    f.seek(0)
    count_words = f.read().split()
    f.seek(0)
    count_letters = 0

    for i in list(map(str.strip, f.readlines())):
        for j in i:
            if j.isalpha():
                count_letters += 1

print('Input file contains:')
print(count_letters, ' letters')
print(len(count_words), ' words')
print(len(count_lines), ' lines')
