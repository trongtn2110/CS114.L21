def dongcot(n, k, p, q):
    
    x = p * 2 + q - 2 - k

    if x <= 0:
        x = p * 2 + q - 2 + k
        if x > n:
            print(-1)
            return
    if x%2 !=0:
        v = 1
        u = x//2 + 1
    else:
        v=2 
        u = x//2
    print(u, end = ' ')
    print(v)
    return

n = int(input())
k = int(input())
p = int(input())
q = int(input())
dongcot(n, k, p, q)