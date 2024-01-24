numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]


def abs_print(num):
    def tuple_abs(item):
        result = 0
        for i in range(len(item)):
            result += item[i]
        return result / len(item)

    print(min(num, key=tuple_abs))
    print(max(num, key=tuple_abs))


abs_print(numbers)
