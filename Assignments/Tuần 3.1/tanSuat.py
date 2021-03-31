from collections import Counter
q = int(input())
c = []
for i in range(q):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    try:
        count_ = Counter(a) 
        c.append(count_[k])
    except:
        c.append(0)
for i in c:
    print(i)