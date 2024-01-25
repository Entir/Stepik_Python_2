def sum_sort(item):
    result = 0
    while item > 0:
        result += item % 10
        item = item // 10
    return result


numbers = sorted([int(i) for i in input().split()])
print(*sorted(numbers, key=sum_sort))
