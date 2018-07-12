#            1
#           / \
#          7   3
#         / \ / \
#        0  2 5  4

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

curr = 0
def leftView(root,lev):
    global curr
    if root == None:
        return
    if lev > curr:
        curr = lev
        print(root.data)
    leftView(root.left,lev+1)
    leftView(root.right,lev+1)


tree=Tree()
tree.root=Node(1)

tree.root.left=Node(7)
#tree.root.left.left = Node(0)
tree.root.left.right = Node(2)

tree.root.right=Node(3)
tree.root.right.left=Node(5)
tree.root.right.right=Node(4)


leftView(tree.root,1)
