arr = []
m, n = map(int, input().split())
for i in range(m):
    arr.append(list(map(int, input().split())))
top, left, bot, right = map(int, input().split())

if top!=0:
    for x in [[0]*n]*top:
        print(*x, sep=' ')

if top == 0:
    for i in range(top, bot+1):
        print(*([0]*left),sep=' ',end ='')
        print(*arr[i][left:(right+1)], sep=' ', end=' ')
        print(*([0]*(n-1-right)), sep=' ')
else:
     for i in range(top, bot+1):
        print(*([0]*left),sep=' ',end =' ')
        print(*arr[i][left:(right+1)], sep=' ', end=' ')
        print(*([0]*(n-1-right)), sep=' ')
if bot!=m-1:
    for x in [[0]*n]*(m-1-bot):
        print(*x, sep=' ')