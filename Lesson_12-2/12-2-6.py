import random
def generate_ip():

    a = random.randrange(1, 255)
    b = random.randrange(0, 255)
    c = random.randrange(0, 255)
    d = random.randrange(1, 255)

    return str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)

print(generate_ip())