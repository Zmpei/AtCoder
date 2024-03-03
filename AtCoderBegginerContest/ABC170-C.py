import sys
x, n = map(int, input().split())
p = list(map(int, input().split()))
if n == 0:
    print(x)
    sys.exit()

not_in_p = []
for i in range(0, 102):
    if i not in p:
        not_in_p.append(abs(x-i))
    else:
        not_in_p.append(102)

ans = not_in_p.index(min(not_in_p))
print(ans)