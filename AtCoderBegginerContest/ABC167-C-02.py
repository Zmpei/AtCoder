n, m, x = map(int, input().split())

books = [0] * n
for _ in range(n):
    books[_] = list(map(int, input().split()))

ans = -1
ans_list = []  # すべてのアルゴリズムについて理解度がxを超えたときの金額リスト
for i in range(1<<n):
    money = 0
    level = [0]*m
    for j in range(n):
        if i>>j & 1:
            money += books[j][0]
            for book in range(m):
                level[book] += books[j][book+1]

    level.sort()
    if level[0] >= x:  # 理解度の最小値がxを超えればよい
        ans_list.append(money)

if len(ans_list) > 0:
    ans = min(ans_list)

print(ans)