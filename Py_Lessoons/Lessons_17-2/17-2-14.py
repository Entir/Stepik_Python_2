file = open('numbers.txt')
num = [int(line.rstrip()) for line in file]
file.close()
print(sum(num))
