def main():
    A, B = map(int, input().split())
    while A > 0 and B > 0:
        if A >= B:
            A %= B
        else:
            B %= A
    return A if B==0 else B


if __name__ == '__main__':
    print(main())