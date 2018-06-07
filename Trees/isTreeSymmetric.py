class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None


s=0
def isTreeSame(root1,root2):
    if root1==None and root2==None:
        return True
    if root1==None or root2==None:
        return False
    return root1.data==root2.data and isTreeSame(root1.left,root2.right) and isTreeSame(root1.right,root2.left)

def isTreeSymmetric(root):
    return isTreeSame(root.left,root.right)


#            5
#           / \
#          2   2
#         / \ / \
#        3  4 4  3
    
tree=Tree()
tree.root=Node(5)

tree.root.left=Node(2)
tree.root.left.left=Node(3)
tree.root.left.right=Node(4)

tree.root.right=Node(2)
tree.root.right.left=Node(4)
tree.root.right.right=Node(3)

print(isTreeSymmetric(tree.root))

#            1
#           / \
#          2   2
#           \   \
#           3    3
    
tree=Tree()
tree.root=Node(1)

tree.root.left=Node(2)
tree.root.left.right=Node(3)

tree.root.right=Node(2)
tree.root.right.right=Node(3)

print(isTreeSymmetric(tree.root))

