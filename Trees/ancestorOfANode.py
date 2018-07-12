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

l = []
def ancestor(root,node):
    if root == None:
        return
    l.append(root.data)
    ancestor(root.left,node)
    ancestor(root.right,node)
    l.pop()
    if root == node:
        print(l)


tree=Tree()
tree.root=Node(1)

tree.root.left=Node(7)
tree.root.left.left = Node(0)
tree.root.left.right = Node(2)

tree.root.right=Node(3)
tree.root.right.left=Node(5)
tree.root.right.right=Node(4)

ancestor(tree.root, tree.root.left.right)
