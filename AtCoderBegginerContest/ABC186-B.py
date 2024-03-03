import numpy as np

h, w = map(int, input().split())
a = list()

min_aij = 999
sum_ai = 0
for i in range(h):
    ai = list(map(int, input().split()))
    a.append(ai)

    min_aij = min(min_aij, min(ai))

for i in a:
    ai = np.array(i)
    ai -= min_aij
    sum_ai += sum(ai)

print(sum_ai)