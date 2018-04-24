class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None

def LCA(root,a,b):
    if root.data<min(a,b):
        return LCA(root.right,a,b)
    elif root.data>max(a,b):
        return LCA(root.left,a,b)
    else:
        return root
                
tree=Tree()
tree.root=Node(10)

tree.root.left=Node(-10)
tree.root.right=Node(30)

tree.root.left.right=Node(8)
tree.root.right.left=Node(25)
tree.root.right.right=Node(60)

tree.root.left.right.left=Node(6)
tree.root.left.right.right=Node(9)
tree.root.right.left.right=Node(28)
tree.root.right.right.right=Node(78)

print(LCA(tree.root,28,78).data)
print(LCA(tree.root,6,30).data)
print(LCA(tree.root,30,78).data)
