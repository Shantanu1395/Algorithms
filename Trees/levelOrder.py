class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None


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
                
tree=Tree()
tree.root=Node(1)

tree.root.left=Node(-1)
tree.root.right=Node(11)

tree.root.left.left=Node(-2)
tree.root.left.right=Node(-3)
tree.root.right.left=Node(21)
tree.root.right.right=Node(6)

tree.root.left.right.right=Node(5)

levelOrder(tree.root)
