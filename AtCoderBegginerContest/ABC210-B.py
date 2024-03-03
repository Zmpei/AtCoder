n = int(input())
s = input()

idx = s.find('1')
ans = 'Takahashi' if idx % 2 == 0 else 'Aoki'

print(ans)