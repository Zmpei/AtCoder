import sys

s = list(input())
t = list(input())

if s == t: print(0), sys.exit()

"""
cnt = 0
for i in range(len(s)):
    if t[i] != s[i]:
        # t[i] = s[i]  # いらない
        cnt += 1
print(cnt)
"""

#  zip関数での別解
res = len([1 for i, j in zip(s, t) if i != j])
print(res)