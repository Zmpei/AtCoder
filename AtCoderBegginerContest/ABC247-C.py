N = int(input())


def retSn(n):
    if n == 1:
        return '1'
    if n == 2:
        return '1 2 1'
    if n >= 3:
        return f'{retSn(n-1)} {n} {retSn(n-1)}'


print(retSn(N))