from decimal import getcontext,Decimal
f =float(input())
c=(5/9)*(f-32)
k=(f+459.67)*(5/9)
getcontext().prec = 6
print(Decimal(c).normalize(),' ',Decimal(k).normalize())