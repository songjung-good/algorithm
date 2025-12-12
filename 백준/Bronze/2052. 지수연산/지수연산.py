from decimal import Decimal, getcontext

n = int(input())

getcontext().prec = n + 10

x = Decimal(2) ** Decimal(-n)
print(format(x, 'f'))
