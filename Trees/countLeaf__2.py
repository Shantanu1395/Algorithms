class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None

def countLeafs(root):
    if root.right==None and root.left==None:
        return 1
    return countLeafs(root.left)+countLeafs(root.right)

tree=Tree()
tree.root=Node(1)

tree.root.left=Node(3)
tree.root.right=Node(2)

tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print(countLeafs(tree.root))
