from decimal import*
x =float(input())
t =x*0.453592/(2.54*2.54)
getcontext().prec = 6
print(Decimal(t).normalize())