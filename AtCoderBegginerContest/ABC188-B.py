import numpy as np

n = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print('Yes' if sum(A*B) == 0 else 'No')