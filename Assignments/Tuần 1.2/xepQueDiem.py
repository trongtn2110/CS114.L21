q = int(input())
a = []
for i in range(0,q):
    b = [int(j) for j in input().split()]
    a.append(b)
for i in a:
    x = i[0]
    y = x
    if x >=4 and x%2==0:
        print(0)
    elif (x < 4):
        print(4-x)
    elif (x > 4) and (x%2!=0):
        while(y%2 != 0):
            y+=1
        print(y-x)