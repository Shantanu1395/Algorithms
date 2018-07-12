#            1
#           / \
#          7   3
#         / \ / \
#        0  2 5  4

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

def level(root, node ,lev):
    if root == None :
        return 0

    if root == node:
        return lev

    l = level(root.left, node, lev+1)

    if not l==0:
        return l

    return level(root.right, node, lev+1)

def isSibbling(root, node1, node2):
    if root == None:
        return False
    return (root.left==node1 and root.right==node2) or (root.left==node2 and root.right==node1) or isSibbling(root.left, node1, node2) or isSibbling(root.right, node1, node2)

def cousinCheck(root, node1, node2):
    level1=level(root, node1, 1)
    level2=level(root, node2, 1)
    if level1 == level2 and (not isSibbling(root, node1,node2)):
        return True
    return False

tree=Tree()
tree.root=Node(1)

tree.root.left=Node(7)
tree.root.left.left = Node(0)
tree.root.left.right = Node(2)

tree.root.right=Node(3)
tree.root.right.left=Node(5)
tree.root.right.right=Node(4)

print(cousinCheck(tree.root,tree.root.left.left,tree.root.right))
print(cousinCheck(tree.root,tree.root.left.left,tree.root.right.right))
