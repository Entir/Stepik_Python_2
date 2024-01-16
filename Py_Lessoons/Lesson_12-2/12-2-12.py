import random

stud = [input() for _ in range(int(input()))]

friend = stud.copy()

for i in range(len(stud)):
    flag = True
    while flag:
        var = random.choice(friend)
        if stud[i] != var:
            print(stud[i] + ' - ' + var)
            friend.remove(var)
            flag = False
