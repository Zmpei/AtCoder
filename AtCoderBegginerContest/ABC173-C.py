h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0
for n in range(1 << h):
    for m in range(1 << w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if n>>i & 1: continue
                if m>>j & 1: continue
                if c[i][j] == '#': cnt += 1
        if cnt == k: ans += 1

print(ans)