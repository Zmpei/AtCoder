n = int(input())
a = list(map(int, input().split()))

for i in range(0, 2002):
    if i not in a:
        print(i)
        break