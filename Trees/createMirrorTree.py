class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self,data):
        self.queue.insert(0,data)
      

    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("Queue Empty!")

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue

    def isEmpty(self):
        return len(self.queue)<=0


def levelOrder(root):
    q=Queue()
    q.enqueue(root)
    while not q.isEmpty():
        temp=q.dequeue()
        print(temp.data,end=" ")
        if temp.left:
            q.enqueue(temp.left)
        if temp.right:
            q.enqueue(temp.right)

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None


s=0
def util(root1,root2):
    if root1==None and root2==None:
        return 
    
    if (not root1==None) and (not root2==None):
        root2.data=root1.data
        
    util(root1.left,root2.right)
    util(root1.right,root2.left)

def convertToMirror(root):
    return util(root.left,root.right)




def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


tree=Tree()
tree.root=Node(5)

tree.root.left=Node(2)
tree.root.left.left=Node(3)
tree.root.left.right=Node(4)

tree.root.right=Node(3)
tree.root.right.left=Node(14)
tree.root.right.right=Node(6)

print("Before")
levelOrder(tree.root)
print()

#            5
#           / \
#          2   3
#         / \ / \
#        3  4 14 6

convertToMirror(tree.root)
print("After")
levelOrder(tree.root)


#            5
#           / \
#          2   2
#         / \ / \
#        3  4 4  3
