from collections import Counter
import numpy as np

N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for i in range(2**N):
    _str = str()
    for j in range(N):
        if (i>>j) & 1:
            _str += S[j]
    ans = max((np.array(list(Counter(_str).values()))==K).sum(), ans)

print(ans)
