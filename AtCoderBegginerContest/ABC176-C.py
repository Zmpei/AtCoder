from sys import stdin
readline = stdin.readline


def main():
    n = int(readline())
    A = list(map(int, readline().split()))

    tallest = A[0]
    cnt = 0

    for height in A:
        if tallest > height:
            cnt += tallest - height
        else:
            tallest = height

    print(cnt)


if __name__ == "__main__":
    main()