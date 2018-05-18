# Tree
#           7
#          / \
#         6   5
#        / \
#       4   3       
#      /
#     1


class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None


def printAllNodesWithKLeaves(root,k):

    if root==None:
        return 0

    if root.left==None and root.right==None:
        return 1

    l=printAllNodesWithKLeaves(root.left,k)
    r=printAllNodesWithKLeaves(root.right,k)

    total=l+r
    
    if total == k:
        print(root.data)

    return total    


tree=Tree()
tree.root=Node(7)
tree.root.left=Node(6)
tree.root.right=Node(5)

tree.root.left.left=Node(4)
tree.root.left.right=Node(3)

tree.root.left.left.left=Node(1)
printAllNodesWithKLeaves(tree.root,1)

