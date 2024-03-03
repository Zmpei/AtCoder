n = int(input())
a = list(map(int, input().split()))

mid = 2**(n-1)

win_l = max(a[:mid])
win_r = max(a[mid:])

second = min(win_l, win_r)

for i, w in enumerate(a):
    if w == second:
        print(i+1)
        break