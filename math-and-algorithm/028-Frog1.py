def main():
    N = int(input())
    H = list(map(int, input().split()))

    dp = [0] * N
    for i in range(1, N):
        if i == 1:
            dp[i] = abs(H[i] - H[i-1])
        else:
            dp[i] = min(dp[i-1] + abs(H[i] - H[i-1]), dp[i-2] + abs(H[i] - H[i-2]))

    return dp[N-1]


if __name__ == '__main__':
    print(main())
