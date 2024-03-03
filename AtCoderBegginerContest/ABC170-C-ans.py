x, n = map(int, input().split())
p = [int(_) for _ in input().split()]

not_in_p = [i for i in range(0, 102) if i not in p]
nip_temp = list(map(lambda s: abs(x - s), not_in_p))

address = nip_temp.index(min(nip_temp))
print(not_in_p[address])
