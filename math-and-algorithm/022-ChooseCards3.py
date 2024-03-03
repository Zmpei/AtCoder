N = int(input())
A = list(map(int, input().split()))

# A_iの出現回数
counter_A = [0 for _ in range(100000)]
for i in range(N):
    counter_A[A[i]] += 1

ans = 0
for i in range(1, 50000):
    ans += counter_A[i] * counter_A[100000-i]
ans += counter_A[50000] * (counter_A[50000] - 1) // 2
print(ans)
# from collections import Counter
#
# N = int(input())
# A = list(map(int, input().split()))
#
# counter_A = Counter(A)
# counter_A_keys = list(counter_A.keys())
#
# cnt = 0
#
# if counter_A[50000] >= 2:
#     cnt += counter_A[50000] * (counter_A[50000]-1) // 2
#
# for i in range(len(counter_A_keys)):
#     if counter_A_keys[i] == 50000:
#         continue
#     for j in range(i+1, len(counter_A_keys)):
#         if counter_A_keys[i]+counter_A_keys[j] == 100000:
#             cnt += counter_A[counter_A_keys[i]]*counter_A[counter_A_keys[j]]
# print(cnt)
