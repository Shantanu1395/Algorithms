class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None


s=0
def util(root1,root2):
    if root1==None and root2==None:
        return 
    
    if (not root1==None) and (not root2==None):
        root2.data=root1.data
        
    util(root1.left,root2.right)
    util(root1.right,root2.left)

def convertToMirror(root):
    return util(root.left,root.right)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

#            5
#           / \
#          3   10
#         / \ / \
#        1  4 14 6

    
tree=Tree()
tree.root=Node(5)

tree.root.left=Node(2)
tree.root.left.left=Node(3)
tree.root.left.right=Node(4)

tree.root.right=Node(3)
tree.root.right.left=Node(14)
tree.root.right.right=Node(6)

print("Before")
inOrder(tree.root)
convertToMirror(tree.root)
print("After")
inOrder(tree.root)
