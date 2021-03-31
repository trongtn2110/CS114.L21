from math import ceil
def mean(a):
    return ((sum(a)) / max(len(a), 1))
a = []
n = int(input())
for i in range(0,n):
    b = []
    m = int(input())
    b[0:m] = [int(y) for y in input().split()]
    a.append(b)
for x in a:     
    print(ceil(mean(x)))