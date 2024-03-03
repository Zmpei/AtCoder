n = int(input())

cnt = 0

for i in range(1, n+1):
    if '7' in str(i):
        cnt += 1

    else:
        oct_i = oct(i)[2:]
        if '7' in oct_i:
            cnt += 1

print(n - cnt)