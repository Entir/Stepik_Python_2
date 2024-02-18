def minutes(x):
    res=[int(i) for i in x.split(':')]
    return res[0]*60+res[1]


with open('logfile.txt', 'r', encoding='utf-8') as file:
    raw = [x.split(', ') for x in [i.rstrip() for i in file.readlines()]]

with open('output.txt', 'w', encoding='utf-8') as out_file:
    for item in raw:
        if minutes(item[2]) - minutes(item[1]) >= 60:
            print(item[0], file=out_file)
