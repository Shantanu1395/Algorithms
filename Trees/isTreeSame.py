#Tree
#      10                      10 
#     /  \                    /  \
#    5    6                  5    6
#        / \                     / \ 
#       8   7                   8   7 
#            \                       \
#             4                       4
class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None


def isTreeSame(root1,root2):
    if root1 == None and root2 == None:
        return True

    if root1 == None or root2 == None:
        return False
    
    return root1.data == root2.data and isTreeSame(root1.left,root2.left) and isTreeSame(root1.right,root2.right)

tree1=Tree()
tree1.root=Node(10)
tree1.root.left=Node(5)
tree1.root.right=Node(6)
tree1.root.right.left=Node(8)
tree1.root.right.right=Node(7)
tree1.root.right.right.right=Node(4)

tree2=Tree()
tree2.root=Node(10)
tree2.root.left=Node(5)
tree2.root.right=Node(6)
tree2.root.right.left=Node(8)
tree2.root.right.right=Node(7)
tree2.root.right.right.right=Node(4)


print(isTreeSame(tree1.root,tree2.root)
