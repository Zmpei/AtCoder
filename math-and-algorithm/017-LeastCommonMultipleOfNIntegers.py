def GCD(a, b):
    while a >= 1 and b >= 1:
        if a >= b:
            a %= b
        else:
            b %= a
    if a >= 1:
        return a
    return b


def LCM(a, b):
    return a * b // GCD(a, b)


N = int(input())
A = list(map(int, input().split()))

R = LCM(A[0], A[1])
for i in range(2, N):
    R = LCM(R, A[i])

print(R)