import numpy as np

n = int(input())
x = np.array(list(map(int, input().split())))

dist1 = abs(x).sum()
dist2 = np.sqrt((abs(x)**2).sum())
dist3 = max(abs(x))

print(dist1, dist2, dist3, sep='\n')