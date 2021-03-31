n = input()
x, y = [int(i) for i in n.split()]
k = y % (2*x)
if k<x:
    print(k)
else:
    print(2*x-k)