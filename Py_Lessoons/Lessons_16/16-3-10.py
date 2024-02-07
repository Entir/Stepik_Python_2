l = [input() for _ in range(int(input()))]


def gem(word):
    total = 0
    for i in word:
        total += ord(i.upper()) - ord('A')
    return total


print(*sorted(l, key=lambda w: (gem(w), w)), sep='\n')
