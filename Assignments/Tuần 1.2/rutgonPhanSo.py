from math import gcd
def RutGon(a):
    x,y = a
    z = gcd(x,y)
    if (y == z):
        print((x//z))
    elif y/z > 1  :
        print((x//z),(y//z))
a = []
n = int(input())
for i in range(0,n):
    b = []
    b = [int(i) for i in input().split()]
    a.append(b)
for i in a:
    RutGon(i)