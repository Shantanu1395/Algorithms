class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None

def InOrder(root):
    if root==None:
        return
    InOrder(root.left)
    print(root.data,end=' ')
    InOrder(root.right)
                
tree=Tree()
tree.root=Node(1)

tree.root.left=Node(-1)
tree.root.right=Node(11)

tree.root.left.left=Node(-2)
tree.root.left.right=Node(-3)
tree.root.right.left=Node(21)
tree.root.right.right=Node(6)

tree.root.left.right.right=Node(5)

InOrder(tree.root)
