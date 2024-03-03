import numpy as np

n = int(input())

ans = 0

for i in range(n):
    a, b = map(int, input().split())
    # ans += np.arange(a, b+1).sum()
    ans += int((b*(b+1) / 2) - (a*(a-1) / 2))

print(ans)