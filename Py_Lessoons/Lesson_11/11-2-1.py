chain = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
DNA = input()
for i in DNA:
    print((chain[i]), sep='', end='')
