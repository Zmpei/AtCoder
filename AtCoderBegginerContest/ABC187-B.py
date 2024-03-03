n = int(input())

xy = list()
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if i == j:
            continue
        elif -1 <= ((xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0])) <= 1:
            cnt += 1
print(cnt)