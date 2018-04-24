class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None


def isItBST(root,minimum,maximum):
    if root==None:
        return True
    
    if(root.data<=minimum or root.data>maximum):
        return False
    
    return  isItBST(root.left,minimum,root.data) and isItBST(root.right,root.data,maximum)     
        
    
"""tree=Tree()
tree.root=Node(10)
tree.root.left=Node(0)
tree.root.left.left=Node(-1)
tree.root.left.right=Node(21)
tree.root.right=Node(25)
tree.root.right.left=Node(16)
tree.root.right.right=Node(32)
"""

tree=Tree()
tree.root=Node(10)
tree.root.left=Node(-10)
tree.root.left.left=Node(-20)
tree.root.left.right=Node(0)
tree.root.right=Node(19)
tree.root.right.left=Node(17)


minimum,maximum=-99999,99999

print(isItBST(tree.root,minimum,maximum))
