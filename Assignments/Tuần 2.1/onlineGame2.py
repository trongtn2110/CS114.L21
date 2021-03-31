import sys
input = sys.stdin.readline
dic = dict()
while True:
    try:
        x = list(map(int, input().split()))
        if x[0] == 0:
            break
        elif x[0] ==1:
            dic[x[1]] = 1
        elif x[0] == 2:
            try:
                if dic[x[1]] == 1:
                    sys.stdout.write("1\n")
                elif dic[x[1]] == 0:
                   sys.stdout.write("0\n")
            except:
                sys.stdout.write("0\n")
        elif x[0] == 3:
                del dic[x[1]]
    except:
        pass