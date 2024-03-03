n, r = map(int, input().split())

N = R = 1
for i, x in enumerate(range(n, n-r, -1)):
    N *= x
    R *= (i+1)

ans = N // R
print(ans)