interval = [i for i in range(int(input()), int(input()) + 1) if '0' not in str(i)]
result = [i for i in interval if all(i % int(x) == 0 for x in str(i))]
print(*result)
