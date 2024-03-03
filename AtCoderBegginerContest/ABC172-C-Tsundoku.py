from collections import deque

N, M, K = map(int, input().split())

bookA = deque(list(map(int, input().split())))
bookB = deque(list(map(int, input().split())))

cnt = 0
while K >= 0:
    if len(bookA) == 0 and len(bookB) == 0:
        break
    elif len(bookA) > 0 and len(bookB) == 0:
        K -= bookA.popleft()
    elif len(bookA) == 0 and len(bookB) > 0:
        K -= bookB.popleft()
    elif len(bookA) > 0 and len(bookB) > 0:
        if bookA[0] <= bookB[0]:
            K -= bookA.popleft()
        else:
            K -= bookB.popleft()
    if K >= 0:
        cnt += 1

print(cnt)