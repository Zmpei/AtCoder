from collections import deque

n = int(input())
d = deque()

a = 1

while a <= n/a:
    if n % a == 0:
        d.append(a)
        if n/a != a:
            d.append(int(n/a))
        else:
            pass
    else:
        pass
    a += 1

d = list(sorted(d))

for ans in d:
    print(ans)