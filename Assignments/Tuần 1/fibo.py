def fibo(x):
    if x <= 2: return 1
    return fibo(x-1) + fibo(x-2)
n = int(input())
if 1<=n<=30:
    print(fibo(n)) 
else:
    print("So",n,"khong nam trong khoang [1,30].")