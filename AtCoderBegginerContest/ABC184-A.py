def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    detA = a * d - b * c

    return print(detA)


if __name__ == '__main__':
    main()