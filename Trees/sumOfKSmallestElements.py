#            9
#           / \
#          2  20
#             / \
#            12  25
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

c=0
s=0
def sumOfKSmallestElements(root,k):
    global c,s 
    if root==None:
        return
    sumOfKSmallestElements(root.left,k)
    s+=root.data
    c+=1
    if c==k:
        print(s)
    sumOfKSmallestElements(root.right,k)
    
tree=Tree()
tree.root=Node(9)

tree.root.left=Node(2)

tree.root.right=Node(20)
tree.root.right.left=Node(12)
tree.root.right.right=Node(25)

sumOfKSmallestElements(tree.root,2)
