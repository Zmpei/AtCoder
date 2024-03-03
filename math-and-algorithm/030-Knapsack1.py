def main():
    N, W = map(int, input().split())
    w, v = [0] * N, [0] * N
    for i in range(N):
        w[i], v[i] = map(int, input().split())
    dp = [[-2**60] * 100009 for _ in range(109)]
    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(W+1):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
    ans = max(max(_) for _ in dp)
    print(ans)
    return


if __name__ == '__main__':
    main()
