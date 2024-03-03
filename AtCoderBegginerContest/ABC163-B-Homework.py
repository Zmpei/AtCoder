n, m = map(int, input().split())
a = list(map(int, input().split()))
days = sum(a)
# print(-1) if n - days < 0 else print(n-days)
print(max(-1, n-days))  # ←賢い