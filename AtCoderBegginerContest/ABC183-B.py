sx, sy, gx, gy = map(int, input().split())

gy = gy * (-1)

a = (gy - sy) / (gx - sx)

# y - sy = a * (x - sx)
# この直線がy = 0を通るときのxの値
# 0 - sy = ax - asx
# ax = asx - sy
# x = sx - (sy / a)

x = sx - (sy / a)

print(x)