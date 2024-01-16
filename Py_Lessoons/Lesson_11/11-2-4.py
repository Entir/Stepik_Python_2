def build_query_string(params: dict):
    txt = []
    for key, value in params.items():
        txt.append(key + '=' + str(value))
    return '&'.join(sorted(txt))

print(build_query_string({'name': 'timur', 'age': 28}))

print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))