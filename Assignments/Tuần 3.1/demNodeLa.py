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
def countNode(r):
    if r is None:
        return 0
    if r.left is None and r.right is None:
        return 1
    return countNode(r.right) + countNode(r.left)
ip = int(input())
r  = Node(ip)
while(True):
    ip = int(input())
    if ip == 0:
        break
    insert(r,ip)
# traverse(r)
print(countNode(r))