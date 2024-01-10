import random
import string

def generate_password(length):
    exclude = 'lI1oO0'
    pasw = ''
    for i in range(length):
        flag = True
        while flag == True:
            x = random.choice(string.ascii_letters + string.digits)
            if x not in exclude:
                pasw += x
                flag = False
    print(pasw)

def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)

n, m = int(input()), int(input())

generate_password(m)
generate_passwords(n, m)
