x, y = map(int, input().split())
ans = 'No'
for t in range(x+1):
    c = x - t
    if 4*t + 2*c == y:
        ans = 'Yes'
print(ans)