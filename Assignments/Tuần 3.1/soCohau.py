def countNumber(x):
    if x == 0:
        return 1
    c = 0
    a = x
    while(a > 0):
        c+=1
        a//=10
    return c
n,m = list(map(int,input().split()))
c_n = countNumber(n)
x = m//(10**c_n)
if m % (10**c_n) >= n:
    print(x- 0 +1 )
elif m % (10**c_n) != n and x == 0:
    print(x+1)
else:
    print(x)