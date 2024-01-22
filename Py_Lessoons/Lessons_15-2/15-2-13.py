def greet(name, *args):
    if len(args) == 0:
        txt = f'Hello, {name}!'
    else:
        txt = f"Hello, {name} and {' and '.join(args)}!"
    return txt


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
