def main():
    N = int(input())
    A = list(map(int, input().split()))

    def GCD(a, b):
        while a > 0 and b > 0:
            if a >= b:
                a %= b
            else:
                b %= a
        return a if b == 0 else b

    for i in range(1, N):
        if i == 1:
            gcd = GCD(A[i-1], A[i])
        else:
            gcd = GCD(gcd, A[i])
    print(gcd)


if __name__ == '__main__':
    main()