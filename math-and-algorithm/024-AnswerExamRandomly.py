N = int(input())

exp = 0
for _ in range(N):
    p, q = map(int, input().split())
    exp += q / p

print(exp)