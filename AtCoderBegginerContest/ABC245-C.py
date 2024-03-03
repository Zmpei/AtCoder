n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = b = 1
for i in range(n-1):
    a_new = b_new = 0
    if a:
        if abs(A[i] - A[i+1]) <= k:
            a_new = 1
        if abs(A[i] - B[i+1]) <= k:
            b_new = 1
    if b:
        if abs(B[i] - A[i+1]) <= k:
            a_new = 1
        if abs(B[i] - B[i+1]) <= k:
            b_new = 1
    a = a_new
    b = b_new

if a + b:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
