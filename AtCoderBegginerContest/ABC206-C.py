import numpy as np
from math import factorial

n = int(input())
a = [int(_) for _ in input().split()]

# cnt = 0
# for i in range(n):
#     for j in a[i+1:]:
#         if a[i] != j:
#             cnt += 1
#
# print(cnt)

_, counts = np.unique(a, return_counts=True)
cnt = counts[counts > 1]
b = 0
for c in cnt:
    b += np.cumsum(range(1, c))[-1]

ans = n * (n-1) // 2 - b
print(ans)