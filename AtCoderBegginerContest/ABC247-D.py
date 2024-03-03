from collections import deque

Q = int(input())
T = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, c = query[1:]
        T.append((x, c))
    elif query[0] == 2:
        c = query[1]
        x, num = T.popleft()
        if c < num:
            subtotal = x * c
            num -= c
            T.appendleft((x, num))
        else:
            subtotal = 0
            while c > num:
                subtotal += x * num
                c -= num
                x, num = T.popleft()
            subtotal += x * c
            num -= c
            if num > 0:
                T.appendleft((x, num))
        print(subtotal)