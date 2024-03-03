from math import sqrt

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

dist_min = 2 * 1e+13
for i in range(N - 1):
    for j in range(i + 1, N):
        dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
        dist_min = min(dist, dist_min)
ret = sqrt(dist_min)
print(f'{ret:.9f}')
