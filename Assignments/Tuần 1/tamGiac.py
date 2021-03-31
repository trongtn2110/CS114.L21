from math import sqrt
def dt(c1,c2,c3):
    p = (c1+c2+c3)/2
    t = (sqrt(p*(p-c1)*(p-c2)*(p-c3)))
    return round(t,2)
c1 = float(input())
c2 = float(input())
c3 = float(input())
if (c1<c2+c3) and (c2<c1+c3) and (c3<c1+c2) and (c1 > 0) and (c2 >0) and (c3 >0):
    if ((c1 == c2) and (c1 != c3)) or ((c2 == c3) and (c2 != c1)) or ((c1 == c3) and (c1 != c2)):
        print("Tam giac can, dien tich =",dt(c1,c2,c3))
    elif (c1 == c2) and (c2 == c3) :
        print("Tam giac deu, dien tich =",dt(c1,c2,c3))
    elif (c1*c1 == c2*c2+c3*c3) or (c2*c2 == c1*c1+c3*c3) or (c3*c3 == c2*c2+c1*c1):
        print("Tam giac vuong, dien tich =",round(dt(c1,c2,c3)))
    else:
        print("Tam giac thuong, dien tich =",dt(c1,c2,c3))
else:
    print("Khong phai tam giac")