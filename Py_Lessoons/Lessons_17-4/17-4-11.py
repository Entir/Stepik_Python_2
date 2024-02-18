with open('class_scores.txt', 'r', encoding='utf-8') as file:
    result = [i.split() for i in [item.rstrip() for item in file.readlines()]]

with open('new_scores.txt', 'w', encoding='utf-8') as out_file:
    for item in result:
        score = int(item[1])
        if score <= 95:
            score = int(item[1]) + 5
        else:
            score = 100
        print(item[0], score, file=out_file)
