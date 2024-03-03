import sys
sys.setrecursionlimit(10**6)

N, K = input().split()
K = int(K)


def f(n, i):
    g1 = int(''.join(sorted(n, reverse=True)))
    g2 = ''.join(sorted(n))

    if len(g2) > 1:
        if g2[0] == '0':
            g2 = g2[1:]

    g2 = int(g2)

    a = str(g1 - g2)

    if n == a:
        return a

    i -= 1
    if i > 0:
        return f(a, i)

    return a


print(f(N, K))