def ktra(x,y):
    for i in range (0,len(x)):
            if x[i] in y:
                return True
    return False
n=int(input())
kq=[]
for i in range (n):
  a=input()
  b=input()
  if ktra(a,b)==True:
    kq.append('YES')
  else:
    kq.append('NO')
for i in range (n):
  print(kq[i])