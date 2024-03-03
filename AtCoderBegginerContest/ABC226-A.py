from decimal import Decimal, ROUND_HALF_UP


x = Decimal(input()).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
print(x)