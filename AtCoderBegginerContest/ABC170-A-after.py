x = list(map(int, input().split()))
ans = 15
for _ in range(len(x)):
    ans -= x[_]

print(ans)