n = int(input())

gaku = int(1.08 * n)
if gaku < 206:
    print('Yay!')
elif gaku == 206:
    print('so-so')
else:
    print(':(')