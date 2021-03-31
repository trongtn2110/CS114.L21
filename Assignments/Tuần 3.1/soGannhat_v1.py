from sys import stdin, stdout
import bisect
n = int(stdin.readline())
a = list([int(x) for x in stdin.readline().split()])
def findNums(a, k, x):
    if x <= a[0]: 
        return a[:k]
    if x >= a[-1]: 
        return a[-k:]
    i = bisect.bisect_left(a, x)
    left, right = i, i+1
    if a[left] == x or x - a[left] <= a[right] - x:
        left -=1
    else:
        right+=1
    for o in range(1,k):
        if left < 0 and right < len(a)-1:
            right+=1
        elif left > 0 and right > len(a)-1:
            left-=1
        elif a[right] == x:
            right +=1
        else:
            if x-a[left] <= a[right]-x:
                left -= 1
            else:
                right += 1
    return a[left+1:right]
while(True):
    z = [int(x) for x in stdin.readline().split()]
    if len(z) == 0:
        break
    result = findNums(a,z[0],z[1])
    print(min(result),max(result))