def main():
    N = int(input())

    ans = 'Yes'
    i = 2
    while i*i <= N:
        if N % i == 0:
            ans = 'No'
            break
        i += 1

    print(ans)


if __name__ == '__main__':
    main()