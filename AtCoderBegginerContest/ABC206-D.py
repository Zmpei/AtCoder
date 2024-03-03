n = int(input())
a = list(map(int, input().split()))

ans = -1

if a == a[::-1]:
    ans = 0

else:
    set_a = set(a)
    for i in set_a:
