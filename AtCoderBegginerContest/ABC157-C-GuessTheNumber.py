import sys

N, M = map(int, input().split())
if N == 1:
    scdict = {1: []}
elif N == 2:
    scdict = {1: [], 2: []}
elif N == 3:
    scdict = {1: [], 2: [], 3: []}

for i in range(M):
    s, c = map(int, input().split())
    scdict[s].append(c)+

num = []
for i, sc in enumerate(scdict.values()):
    if len(sc) == 0:
        scdict[i + 1].append(0)
    if len(sc) >= 2 and 0 in sc:
        sc.remove(0)
    num.append(min(sc))

if N >= 2:
    if num[0] == 0:
        print('-1')
        sys.exit()

for i in num:
    print(i, end='')