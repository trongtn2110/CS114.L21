n,m = [int(i) for i in input().split()]
p,q = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append(input().split())
if m*n == p*q:
        k =0
        for i in a:
            for j in i:
                print(j,end=' ')
                k+=1
                if k == q:
                    k = 0
                    print()
else:
    for i in a:
        for j in i:
            print(j,end=' ')
        print()