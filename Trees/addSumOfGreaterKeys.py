class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None


s=0
def addSumOfGreaterKeys(root):
    global s
    if root:
        addSumOfGreaterKeys(root.right)
        s+=root.data
        root.data=s
        addSumOfGreaterKeys(root.left)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
    
tree=Tree()
tree.root=Node(5)
tree.root.left=Node(2)
tree.root.right=Node(13)

addSumOfGreaterKeys(tree.root)
inOrder(tree.root)

#           5
#          / \
#         2   13
