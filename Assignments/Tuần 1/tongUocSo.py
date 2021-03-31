n = int(input())
tong = 0
for x in range(1,n):
    if (n % x == 0):
        tong += x
print(tong)