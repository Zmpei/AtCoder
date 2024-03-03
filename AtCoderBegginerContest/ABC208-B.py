from math import factorial

p = int(input())

cnt = 0
for i in range(10, 0, -1):
    while p >= factorial(i):
        cnt += 1
        p -= factorial(i)

print(cnt)