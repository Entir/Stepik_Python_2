import random, string
def generate_index():
    a = random.choice(string.ascii_uppercase)
    b = random.choice(string.ascii_uppercase)
    e = random.choice(string.ascii_uppercase)
    f = random.choice(string.ascii_uppercase)
    c = str(random.randrange(0, 100))
    d = str(random.randrange(0, 100))

    return a + b + c + '_' + d + e + f

print(generate_index())