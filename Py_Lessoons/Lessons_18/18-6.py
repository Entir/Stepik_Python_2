with open('forbidden_words.txt', 'r', encoding='utf-8') as b_file:
    bad = b_file.readline().split()

#name = input()
name = 'data.txt'
with open(name, 'r', encoding='utf=8') as file:
    s = file.read()

s_lower = s.lower()

for i in bad:
    s_lower = s_lower.replace(i, '*'*len(i))

result = ''
for i in range(len(s_lower)):
    if s_lower[i] == '*':
        result += '*'
    elif s_lower[i] != '*' and s_lower[i] != s[i]:
        result += s[i]
    else:
        result += s_lower[i]

print(result)
