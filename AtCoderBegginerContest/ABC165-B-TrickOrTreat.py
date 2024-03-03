x = int(input())
balance = 100
count = 0

while x > balance:
    balance = int(balance*1.01)
    count += 1

print(count)