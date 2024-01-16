def merge(values: list):
    result = {}

    for item in values:
        for key, val in item.items():
            if key not in result:
                result[key] = {val}
            else:
                result[key].update({val})

    return result

res = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100},
             {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])

print(res)
