def main():
    N = int(input())
    n = N
    ans = []
    i = 2
    while i*i <= N:
        if n % i != 0:
            i += 1
            continue
        ans.append(i)
        n //= i
        i = 2
    if n != 1:
        ans.append(n)
    ans.sort()

    print(*ans)


if __name__ == '__main__':
    main()