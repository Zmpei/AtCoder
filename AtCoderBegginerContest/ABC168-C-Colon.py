import math
a, b, h, m = map(int, input().split())

rh = h*30 + m*0.5
rm = m*6
angleC = math.radians(abs(rh - rm))
if angleC > math.pi:
    angleC = math.pi*2 - angleC

c = a**2 + b**2 - 2*a*b * math.cos(angleC)
print(math.sqrt(c))
