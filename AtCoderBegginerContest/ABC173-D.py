n = int(input())
a = list(map(int, input().split()))
con = 0
con = sum(a) - min(a)
print(con)