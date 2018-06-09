#            1
#           / \
#          2   3
#         / \ / \
#        4   56  3
#              \  \
#               8  9
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

l=[]
temp=[]
m=-1
def distinctNodesInRootToLeaf(root):
    global l,temp,m
    if root==None:
        return
    l.append(root.data)
    distinctNodesInRootToLeaf(root.left)
    distinctNodesInRootToLeaf(root.right)
    if len(set(l))>m:
        m=len(set(l))
        temp=list(l)
    l.pop()    
    
tree=Tree()
tree.root=Node(1)

tree.root.left=Node(2)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

tree.root.right=Node(3)

tree.root.right.left=Node(6)
tree.root.right.left.right=Node(8)

tree.root.right.right=Node(3)
tree.root.right.right.right=Node(9)

distinctNodesInRootToLeaf(tree.root)
print(temp)
