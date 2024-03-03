n = int(input())

ablist = []

for a in range(2, n-1):
    for b in range(a, n):
        if a ** b <= n:
            ablist.append(a ** b)
        else:
            break

ans = sum([1 for _ in range(1, n+1) if _ not in ablist])
print(ans)
