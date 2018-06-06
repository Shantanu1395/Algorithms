#       Tree
#        43
#       /  \
#      30  50
#     / \  
#    20 35
#   /
#  10

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

c=0

def KthLargestElement(root,k):
    global c
    if root==None or c>=k:
        return 

    KthLargestElement(root.right,k)
    c+=1
    if c==k:
        print(root.data)
    KthLargestElement(root.left,k)



tree=Tree()
tree.root=Node(43)
tree.root.left=Node(30)
tree.root.right=Node(50)

tree.root.left.left=Node(20)
tree.root.left.right=Node(35)

tree.root.left.left.left=Node(10)
KthLargestElement(tree.root,2)
