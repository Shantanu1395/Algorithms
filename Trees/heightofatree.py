class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None


def height(root):
    if root == None:
        return 0
    return max(height(root.right),height(root.left))+1

tree=Tree()
tree.root=Node(10)
tree.root.left=Node(5)
tree.root.right=Node(6)
tree.root.right.left=Node(8)
tree.root.right.right=Node(7)
tree.root.right.right.right=Node(4)
print(height(tree.root))
