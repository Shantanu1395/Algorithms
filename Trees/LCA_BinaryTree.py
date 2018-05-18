# Tree
#           3
#          / \
#         6   8
#        / \    \
#       2   11   13
#           / \  /
#          9   5 7


class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def  __init__(self):
        self.root=None

def LCA(root,a,b):
    
    if root.data==a:
        return a
    if root.data==b:
        return b

    if root.left==None or root.right==None:
        return -1

    left=LCA(root.left,a,b)
    right=LCA(root.right,a,b)
    if(left!=-1 and right!=-1):
        return root.data
    else:
        return max(left,right)
            
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

print(LCA(tree.root,2,5))
#Output - 6
print(LCA(tree.root,2,8))
#Output - 3
print(LCA(tree.root,9,5))
#Output - 11
print(LCA(tree.root,9,3))
#Output - 3
