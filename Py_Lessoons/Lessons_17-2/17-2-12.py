name = input()
file = open(name)
txt = [line.rstrip() for line in file]
file.close()
print(txt[-2])
