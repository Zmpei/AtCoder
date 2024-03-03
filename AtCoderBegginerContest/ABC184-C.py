def change(a, b, p):
    for c in range(K):
        for d in range(K):
            if ((a + b) == (c + d)) or ((a - b) == (c - d)) or (abs(a - c) + abs(b - d)) <= 3:
                if grid[c][d] == -1:
                    grid[c][d] = p + 1


K = 21
grid = [[-1] * K for _ in range(K)]
grid[K // 2][K // 2] = 0

for i in range(10):
    for a in range(K):
        for b in range(K):
            if grid[a][b] == i:
                change(a, b, i)

for row in grid:
    print(*row)


def main():
    # 0手
    if a == c and b == d:
        return 0

    # 1手
    if a + b == c + d:
        return 1
    if a - b == c - d:
        return 1
    if abs(a - c) + abs(b - d) <= 3:
        return 1

    # 2手
    if abs(a - c) + abs(b - d) <= 6:
        return 2
    if (abs(a - c) + abs(b - d)) % 2 == 0:
        return 2
    if abs((a + b) - (c + d)) <= 3:
        return 2
    if abs((a - b) - (c - d)) <= 3:
        return 2

    # 3手
    return 3


a, b = map(int, input().split())
c, d = map(int, input().split())

if __name__ == '__main__':
    print(main())