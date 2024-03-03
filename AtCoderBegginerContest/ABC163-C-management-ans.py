n = int(input())
a = list(map(int, input().split()))

member = [0] * n
for i in a:
    member[i-1] += 1

print(*member, sep='\n')  # *list 便利