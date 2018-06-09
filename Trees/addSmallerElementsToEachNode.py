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
def addSmallerElementsToEachNode(root):
    global s
    if root==None:
        return
    addSmallerElementsToEachNode(root.left)
    s+=root.data
    root.data=s
    addSmallerElementsToEachNode(root.right)
    
    
tree=Tree()
tree.root=Node(9)

tree.root.left=Node(6)
tree.root.left.left=Node(3)

tree.root.right=Node(15)
tree.root.right.right=Node(21)

#            9
#           / \
#          6   15
#         /     \
#        3       21
levelOrder(tree.root)
print()

addSmallerElementsToEachNode(tree.root)

#            18
#           / \
#          9   33
#         /     \
#        3       54
levelOrder(tree.root)
