def main():
    N = int(input())

    primes = []
    for i in range(2, N+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)

    for p in primes:
        print(p, end=' ')
    print()  # 最後の改行


if __name__ == '__main__':
    main()