from collections import Counter
import copy

n = int(input())
a = list(map(int, input().split()))

"""
標準ライブラリのcollections.Counter()で同様の操作ができる
生成されるのは`Counter`オブジェクト
a_set = set(a)
a_all = {}
for i in a_set:
    a_all[i] = int(cnt)
"""

cllct = dict(Counter(a))
for k, v in cllct.items():
    cnt = 0
    cnt += (v * (v - 1)) / 2
    a_all = dict(k, v)