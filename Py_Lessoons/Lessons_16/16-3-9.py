data = input().split()
print(*sorted(sorted(data), key=lambda x: x.lower()))
