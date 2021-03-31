from math import ceil
n,m,a = [int(i) for i in input().split()]
b = ceil(n/a)
c = ceil(m/a)
print(b*c)