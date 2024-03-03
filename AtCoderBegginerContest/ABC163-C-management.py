n = int(input())
a = {}
for i in range(1, n+1):
    a[i] = []

member = list(map(int, input().split()))
for i in member:
    a[i].append(1)

for j in a:
    print(len(a[j]))