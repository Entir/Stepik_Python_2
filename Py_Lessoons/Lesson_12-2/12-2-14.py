import random
import string


def generate_password(length):
    exclude = 'lI1oO0'

    letters = [[x for x in string.ascii_uppercase if x not in exclude],
               [x for x in string.ascii_lowercase if x not in exclude],
               [x for x in string.digits if x not in exclude]]

    pasw = [random.choice(letters[0]),
            random.choice(letters[1]),
            random.choice(letters[2])]

    for i in range(length - 3):
        flag = True
        while flag:
            x = random.choice(string.ascii_letters + string.digits)
            if x not in exclude:
                pasw.append(x)
                flag = False
    random.shuffle(pasw)
    print(*pasw, sep='')


def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)


n, m = int(input()), int(input())

generate_passwords(n, m)
