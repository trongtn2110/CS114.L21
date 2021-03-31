k =list(input().split(" "))
t = int(k[0])
c = int(k[1])
for g in range(0,t+1):
    ch = t - g
    if 2*g + 4*ch == c:
        print(g,ch)