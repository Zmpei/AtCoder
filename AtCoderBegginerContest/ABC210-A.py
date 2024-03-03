n, a, x, y = map(int, input().split())

if a >= n:
    ans = n*x
else:
    ans = a*x + (n-a)*y

print(ans)