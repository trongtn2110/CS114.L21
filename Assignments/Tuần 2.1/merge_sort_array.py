n,m = [int(i) for i in input().split()]
a= []
b= []
a[:n] = [int(i) for i in input().split()]
b[:m] = [int(i) for i in input().split()]
a = (a+b)
a.sort()
for i in a :
    print(i, end = " ")