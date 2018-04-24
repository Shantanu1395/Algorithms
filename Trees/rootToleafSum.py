class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None


def rootToleafSum(root,amount):
    if root == None:
        return False

    if root.left==None and root.right==None and amount==root.data:
        return True

    return rootToleafSum(root.left,amount-root.data) or rootToleafSum(root.right,amount-root.data)
   
tree=Tree()
tree.root=Node(10)
tree.root.left=Node(16)
tree.root.left.right=Node(-3)
tree.root.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(11)
amount=26

print(rootToleafSum(tree.root,amount))
