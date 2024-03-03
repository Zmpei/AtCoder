n = int(input())
tuple_a = tuple(map(int, input().split()))

cnt_ans = 0
for i in range(2, max(tuple_a) + 1):
    cnt = 0
    for j in range(n):
        if tuple_a[j] % i == 0:
            cnt += 1

    if cnt > cnt_ans:
        cnt_ans = cnt
        ans = i

print(ans)