abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]
r = 2

coordinates = zip(abscissas, ordinates, applicates)
result = all(map(lambda x: True if x[0]**2 + x[1]**2 + x[2]**2 <= r**2 else False, coordinates))
print(result)
