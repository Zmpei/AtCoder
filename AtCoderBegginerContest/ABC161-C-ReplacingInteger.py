import sys
n, k = map(int, input().split())

n = abs(n - k)

if k == n:
    print(0)
    sys.exit()
elif k > n:
    print(min(n, k-n))
    sys.exit()
else:
    while n > k:
        n %= k
    print(min(n%k, abs(n-k)))