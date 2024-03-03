n, x = map(int, input().split())
s = input()

for i in s:
    if i == 'o':
        x += 1
    elif i == 'x':
        if x > 0:
            x -= 1
        else:
            pass

print(x)