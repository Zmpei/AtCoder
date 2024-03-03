a, b, c, d, e, f, x = map(int, input().split())


def func(a, b, c, x, ans=0):
    if x <= 0:
        return ans
    if x >= a:
        ans += a * b
        x -= a + c
    else:
        ans += x * b
        x -= a
    return func(a, b, c, x, ans)


dist_t = func(a, b, c, x)
dist_a = func(d, e, f, x)

if dist_t == dist_a:
    print('Draw')
elif dist_t > dist_a:
    print('Takahashi')
else:
    print('Aoki')