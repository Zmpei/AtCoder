from collections import deque
n, m = map(int, input().split())
INF = 100000000

to = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
print('Yes')
q = deque([])
dist = [INF] * n
prev = [-1] * n
dist[0] = 0
q.append(0)

while len(q) > 0:
    v = q.popleft()
    for i in to[v]:
        if dist[i] != INF:
            continue
        dist[i] = dist[v] + 1
        prev[i] = v
        q.append(i)
for i in range(1, n):
    ans = prev[i]
    ans += 1
    print(ans)

