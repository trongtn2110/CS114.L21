def _count_num(y):
    dem = 0
    while y > 0:
        y = y//10
        dem = dem + 1
    return dem
def _Is_Armtrong(x):
    y =x
    num = _count_num(y)
    _sum = 0
    while y > 0:
        a = y%10
        _sum = _sum + a**num
        y = y //10
    if x == _sum:
        return True
    else:
        return False

a = int(input())
print(_Is_Armtrong(a))