N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

expB = sum(B) / N
expR = sum(R) / N

print(expB + expR)
