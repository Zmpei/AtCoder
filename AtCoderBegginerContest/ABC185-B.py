n, m, t = map(int, input().split())

x = n  # ある時刻での電池残量
ans = 'Yes'
a0 = b0 = 0

for i in range(m):
    a1, b1 = map(int, input().split())

    if i == 0:
        if n < a1:
            ans = 'No'
            break

    # 前回休憩終了時刻から今回休憩までに減った電池残量
    x -= (a1 - b0)

    # 電池残量が0を下回ったかの判定
    if x <= 0:
        ans = 'No'
        break

    # 今回の休憩で増えた電池残量
    x = min((x + b1 - a1), n)

    # 前回休憩時刻の更新
    a0 = a1
    b0 = b1

x -= (t - b0)
if x <= 0:
    ans = 'No'

print(ans)