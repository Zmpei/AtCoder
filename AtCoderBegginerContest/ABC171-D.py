n = int(input())
a = list(map(int, input().split()))
q = int(input())
x = [0] * 100001
ans = sum(a)

for ai in a:
    x[ai] += 1  # xのなかでaiが登場する個数のカウント

for _ in range(q):
    b, c = map(int, input().split())
    ans += (c-b) * x[b]
    x[c] += x[b]  # bをcに入れ替えた個数だけcが増加する
    x[b] = 0
    print(ans)

# for i in range(q):
#     count = 0
#     b, c = map(int, input().split())
#
#     for j in a:
#         if j == b:
#             a[count] = c
#         count += 1
#     a_list = [_ for _ in a]
#     ans.append(a_list)
#
# for answer in ans:
#     print(sum(answer))
