import numpy as np
from collections import Counter

N = int(input())
S = []
T = []
ans = 'Yes'
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)
A = np.array(list(zip(S, T))).flatten()
A = Counter(A)
for i in range(N):
    if S[i] == T[i]:  # 姓名おなじパターン
        if A[S[i]] > 2:
            S[i] = ''
    elif A[S[i]] > 1:  # 姓名ちがうパターン
        S[i] = ''
    if S[i] == T[i]:
        if A[T[i]] > 2:
            T[i] = ''
    elif A[T[i]] > 1:
        T[i] = ''
    if S[i] == T[i] == '':
        ans = 'No'
        break
print(ans)