N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

exp = (sum(A) + sum(B) * 2) / 3
print(exp)