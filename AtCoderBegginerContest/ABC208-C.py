import numpy as np

n, k = map(int, input().split())

a = list(map(int, input().split()))
a_sorted = sorted(a)
a_sorted = np.array(a_sorted)

base = k // n
bonus_num = k % n

bonus_idx = list(map(lambda x: a.index(x), a_sorted[:bonus_num]))

# bonus_idx = []
# for _ in a_sorted[:bonus_num]:
#     bonus_idx.append(a.index(_))

ans = np.array([base]*n)
ans[bonus_idx] += 1

print('\n'.join(list(map(str, ans))))
# for i in a:
#     if a_sorted.index(i) < bonus_num:
#         print(base + 1)
#     else:
#         print(base)