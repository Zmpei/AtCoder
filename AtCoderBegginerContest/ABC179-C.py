def main():
    import sys
    import numpy as np
    import itertools

    input = sys.stdin.readline

    n = int(input())
    list_nc = list(range(1, n))
    cnt = 0
    combo = [[0]] * (n - 1)

    for i, nc in enumerate(list_nc):
        a = b = list(range(1, nc+1))
        combo[i] = list(itertools.product(a, b))

    for i, list_ab in enumerate(combo):
        for ab in list_ab:
            if ab[0] * ab[1] == list_nc[i]:
                cnt += 1
            else:
                pass

    print(cnt)


if __name__ == '__main__':
    main()