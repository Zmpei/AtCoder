import sys

input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

mid = N // 2
left, right = 0, N-1

ans = 'No'
while left <= right:
    if X == A[mid]:
        ans = 'Yes'
        break
    elif X < A[mid]:
        right = mid - 1
        mid = (right + left) // 2
    elif X > A[mid]:
        left = mid + 1
        mid = (right + left) // 2
print(ans)