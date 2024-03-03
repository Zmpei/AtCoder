def main():
    N = int(input())

    for i in range(1, int(N**(1/2))+1):
        if N % i != 0:
            continue
        print(i)
        if N / i != i:
            print(int(N / i))


if __name__ == '__main__':
    main()