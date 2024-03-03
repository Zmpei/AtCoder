x, y = map(int, input().split())

a = max(x, y)
b = min(x, y)

print('Yes' if a - (b + 3) < 0 else 'No')