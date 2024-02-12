name = input()
file = open(name)
for line in file:
    print(line.rstrip())
file.close()
