n, m = map(int, input().split())
a = list(map(int, input().split()))

A = sum(a)
count = 0
for i in a:
    if i >= A / (4*m):
        count += 1

if count >= m:
    print('Yes')
else:
    print('No')
