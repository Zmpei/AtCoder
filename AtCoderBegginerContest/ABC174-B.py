import numpy as np

n, d = map(int, input().split())
dist = list()

for i in range(n):
    x, y = map(int, input().split())
    distance = np.sqrt(x**2 + y**2)
    dist.append(distance)

cnt = sum(abs(i) <= d for i in dist)
print(cnt)