from decimal import Decimal 
import decimal
decimal.getcontext().prec = 300
x1, y1, x2, y2, x3, y3 = [Decimal(item) for item in input().split(',')]
x13, y13 = x1 - x3, y1 - y3
x23, y23 = x2 - x3, y2 - y3
S = abs(x13 * y23 / 2 - x23 * y13 / 2)
print(S)