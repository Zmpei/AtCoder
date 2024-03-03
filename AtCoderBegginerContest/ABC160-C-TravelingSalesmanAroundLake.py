k, n = map(int, input().split())
a = list(map(int, input().split()))
a.append(a[0])
dist = []
for i in range(n):
    dist.append(abs(a[i+1] - a[i]))
for i in range(len(dist)):
    if dist[i] > k/2:
        dist[i] = k - dist[i]

print(sum(dist) - max(dist))