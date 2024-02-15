with open('input.txt', 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf=8') as f_out:
    buf = list(enumerate(f_in.readlines(), start=1))
    for count, value in buf:
        print(f'{count}) {value}', end='', file=f_out)
