N = int(input())

exp = 0
for i in range(N):
    exp += N / (N - i)
print(exp)