file = open('nums.txt')
num = [int(i) for i in file.read().split()]
file.close()
print(sum(num))
