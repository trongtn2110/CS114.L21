x = input()
y = input()
a = len(x)
b=""
while a > 0:
    b = b + x[a-1]
    a-=1
if y == b:
    print("YES")
else:
    print("NO")