# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 配列初期化
dp = [[0] * (S + 1) for _ in range(N + 1)]

cnt = 0
for i in range(1, N + 1):
    for j in range(1, S + 1):
        if j < A[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + A[i-1])
    if dp[i][S] == S:
        cnt += 1

print('Yes' if cnt > 0 else 'No')