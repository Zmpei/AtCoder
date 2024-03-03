n = int(input())
items = {}

for i in range(n):
    item = input()
    items[item] = True

print(len(items))
