with open('grades.txt', 'r', encoding='utf-8') as file:
    stud = [x.split() for x in [i.rstrip() for i in file.readlines()]]

result = list(map(lambda x: x[0], filter(lambda i: int(i[1]) >= 65 and int(i[2]) >= 65 and int(i[3]) >= 65, stud)))

print(len(result))
