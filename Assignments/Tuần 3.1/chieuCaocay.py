from sys import stdin
from collections import deque
class Node:
    def __init__(self, key ):
        self.left = None      
        self.right = None
        self.val = key
def insertN(root,key):
    if root is None :
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insertN(root.right, key)
        else:
            root.left = insertN(root.left, key)
    return root
def insertL2T(r,l):
    for i in l:
        r = insertN(r,i)
    return r
def countHigh(r,count = 0):
    if r is None:
        return count
    count += 1
    return max(countHigh(r.left,count),countHigh(r.right,count))
d = deque()
while(True):
    a = list(map(int,stdin.readline().split()))
    if a[0] == 0:
        d.appendleft(a[1])
    elif a[0] == 1:
        d.append(a[1])
    elif a[0] ==2 :
        if len(d) > 0:
            try:
                d.insert(d.index(a[1])+1,a[2])
            except ValueError:
                d.appendleft(a[2])
    else:
        r = Node((d[0]))
        r = insertL2T(r,d)
        print(countHigh(r))
        exit()