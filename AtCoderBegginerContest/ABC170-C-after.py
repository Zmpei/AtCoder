import sys
x, n = map(int, input().split())
p = [int(_) for _ in input().split()]

if n == 0:
    print(x)
    sys.exit()

not_in_p = []
for i in range(0, 102):
    if i not in p:
        not_in_p.append(i)

nip_temp = []
for i in not_in_p:
    nip_temp.append(abs(x-i))

address = nip_temp.index(min(nip_temp))
print(not_in_p[address])
