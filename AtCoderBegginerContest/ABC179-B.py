def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    cnt = 0

    for _ in range(n):
        d1, d2 = map(int, input().split())

        if d1 == d2:
            cnt += 1
        else:
            if cnt >= 3:
                pass
            else:
                cnt = 0

    print('Yes' if cnt >= 3 else 'No')


if __name__ == '__main__':
    main()
