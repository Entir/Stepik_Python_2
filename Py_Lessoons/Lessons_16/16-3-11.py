ip = [input() for _ in range(int(input()))]


def adr(item: list):
    i = item.split('.')
    return (int(i[0]) * 256**3 +
            int(i[1]) * 256**2 +
            int(i[2]) * 256**1 +
            int(i[3]) * 256**0)


print(*sorted(ip, key=lambda w: adr(w)), sep='\n')
