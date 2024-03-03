n = input()

if sum(list(map(int, list(n)))) % 3 == 0:
    print(0)
    exit()

ans = 0

for i in range(1, 2 ** len(n)):
    sum_ans = 0
    cnt = 0
    for j in range(len(n)):
        if i >> j & 1:
            sum_ans += int(n[j])
            cnt += 1

    if sum_ans % 3 == 0:
        ans = max(ans, cnt)

print(len(n) - ans if ans > 0 else -1)