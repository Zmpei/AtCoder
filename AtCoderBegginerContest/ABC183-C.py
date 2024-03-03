from itertools import permutations

n, k = map(int, input().split())

list_t = [[]] * n
for i in range(n):
    list_t[i] = list(map(int, input().split()))

cnt = 0
for perms in permutations(range(1, n)):
    time = 0
    last = 0
    for i, j in enumerate(perms):
        if i == 0:
            time += list_t[0][j]
            last = j
        else:
            time += list_t[last][j]
            last = j

    else:
        time += list_t[last][0]

    if time == k:
        cnt += 1

print(cnt)