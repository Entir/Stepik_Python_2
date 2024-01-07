txt = input().split()
dict_txt = {}

for i in txt:
    if i not in dict_txt:
        dict_txt[i] = 1
        print(dict_txt[i], end=" ")
    else:
        dict_txt[i] += 1
        print(dict_txt[i], end=" ")
