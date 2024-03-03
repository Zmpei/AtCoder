a, b, c, d = map(int, list(input()))

for i in range(1<<3):
    num = [a, b, c, d]
    for j in range(3):
        if i>>j & 1 != 1:  # 1桁目==1 がTrueではなかった場合
            num[j+1] *= -1
    ans = sum(num)
    if ans == 7:
        for k, n in enumerate(num):
            if n >= 0 and k > 0:  # 先頭には'+'をつけたくない
                print('+', n, sep='', end='')
            else:
                print(n, sep='', end='')
        else:
            print('=7', sep='')
        break