def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    mtx = [[value]*m for _ in range(n)]
    return mtx


if __name__ == '__main__':
    print(matrix())
    print(matrix(3))
    print(matrix(2, 5))
    print(matrix(3, 4, 9))
