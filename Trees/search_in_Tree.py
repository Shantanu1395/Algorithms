class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def  __init__(self):
        self.root=None

def search(root,data):
    if root==None:
        return False
    return root.data==data or search(root.left,data) or search(root.right,data)
            
tree=Tree()
tree.root=Node(3)

tree.root.left=Node(6)
tree.root.right=Node(8)

tree.root.left.left=Node(2)
tree.root.left.right=Node(11)
tree.root.right.right=Node(13)

tree.root.left.right.left=Node(9)
tree.root.left.right.right=Node(5)
tree.root.right.right.left=Node(7)

print(search(tree.root,123))
print(search(tree.root,2))
