#            1
#           / \
#          7   3
#             / \
#             5  4
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

l=[]
def kSumPaths(root,k):
    global l
    if root==None:
        return
    l.append(root.data)
    kSumPaths(root.left,k)
    kSumPaths(root.right,k)
    s=0
    for i in l:
        s+=i
        if k==s:
            print(l)
    l.pop()

tree=Tree()
tree.root=Node(1)

tree.root.left=Node(7)

tree.root.right=Node(3)
tree.root.right.left=Node(5)
tree.root.right.right=Node(4)

kSumPaths(tree.root,8)
