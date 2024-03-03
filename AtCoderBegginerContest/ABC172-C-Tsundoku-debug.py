from collections import deque
import random

#  リストの先頭だけ見ても最適解は出ない
"""
def mine(k, a, b):
    bookA = deque(a)
    bookB = deque(b)

    cnt = 0
    r = k
    while r > 0:
        if len(bookA) == 0 and len(bookB) == 0:
            break
        elif len(bookA) > 0 and len(bookB) == 0:
            r -= bookA.popleft()
        elif len(bookA) == 0 and len(bookB) > 0:
            r -= bookB.popleft()
        elif len(bookA) > 0 and len(bookB) > 0:
            if bookA[0] <= bookB[0]:
                r -= bookA.popleft()
            else:
                r -= bookB.popleft()
        if r >= 0:
            cnt += 1
    return cnt
"""


#  解答
def tsundoku():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    da = [0]
    db = [0]
    for i in range(n):
        da.append(da[i] + a[i])
    for i in range(m):
        db.append(db[i] + b[i])

    cnt = 0
    j = m
    for i in range(n+1):
        if da[i] > k:
            break
        while db[j] > k - da[i]:
            j -= 1
        cnt = max(cnt, i+j)

    return print(cnt)


tsundoku()

"""
for t in range(100):
    n = random.randint(1, 200000)
    m = random.randint(1, 200000)
    k = random.randint(1, 1000000000)
    a = [random.randint(1, 1000000000) for i in range(n)]
    b = [random.randint(1, 1000000000) for i in range(m)]

    res1 = mine(k, a, b)
    res2 = answer(n, m, k, a, b)
    if res1 != res2:
        print(res1, end=' ')
        print(res2, end=' \t')
        print(a[0:3], b[0:3])
        print(k)
"""