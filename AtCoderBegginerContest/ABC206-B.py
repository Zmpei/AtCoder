n = int(input())

ans = 0
for i, k in enumerate(range(1, n+1)):
    ans += k
    if ans >= n:
        print(i+1)
        break