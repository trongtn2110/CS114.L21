import sys
a = []
n,m = map(int, sys.stdin.readline().split())
maxx = [0]*m
for i in range(n):
    ls = list(map(str,map(int,sys.stdin.readline().split())))
    a.append(ls)
for i in range(m):
    maxx[i] = max([len(ls[i]) for ls in a])
for i in range(n):
    for j in range(m):
        if j == m-1:
            print(' '*(maxx[j]-len(a[i][j])) + a[i][j])
        else:
            print(' '*(maxx[j]-len(a[i][j])) + a[i][j], end = ' ')