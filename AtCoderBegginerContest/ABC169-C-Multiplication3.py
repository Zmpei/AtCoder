import math
from decimal import Decimal
a, b = map(Decimal, input().split())
ans = a * b
print(math.floor(ans))

# S = list(input().split())
# a = int(S[0])
# b = S[1].replace('.', '')
# B = int(b)
#
# ans = (a * B) // 100
# print(ans)

# a, b = input().split()
# A = int(a)
# b = b.replace('.', '')
# B = int(b)
# ans = (A * B) // 100
# print(ans)

# S = list(input().split())
# a = int(S[0])
# b = float(S[1])  # 小数点をfloat型にすると限りなく近似された値が2進数として処理されるが厳密に等しくなるわけではない
#
# ans = int((a * b) // 1)
# print(ans)
