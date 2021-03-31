dic = dict()
kq = []
while True:
    x = list(map(int, input().split()))
    if x[0] == 0:
        break
    elif x[0] ==1:
        dic[x[1]] = 1
    elif x[0] == 2:
        try:
            if dic[x[1]] == 1:
                kq.append(1)
        except KeyError:
            kq.append(0)
    
print(*kq, sep="\n")