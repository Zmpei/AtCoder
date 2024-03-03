from collections import Counter

N = int(input())
A = Counter(map(int, input().split()))

ans = A[100] * A[400] + A[200] * A[300]
print(ans)

