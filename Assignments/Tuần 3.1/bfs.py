class Node:
    def __init__(self, key):
        self.left = None      
        self.right = None
        self.val = key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
def traverse(rootnode):
    thislevel = [rootnode]
    while thislevel:
        nextlevel = list()
        for n in thislevel:
            print (n.val,end=" ")
            if n.left: nextlevel.append(n.left)
            if n.right: nextlevel.append(n.right)        
        thislevel = nextlevel
ip = int(input())
r  = Node(ip)
while(True):
    ip = int(input())
    if ip == 0:
        break
    insert(r,ip)
traverse(r)