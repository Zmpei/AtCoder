import sys
k = int(input())
a, b = map(int, input().split())
dist = list(range(a, b+1))

for d in dist:
    if d % k == 0:
        print('OK')
        sys.exit()

print('NG')