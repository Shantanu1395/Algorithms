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
        for i in self.queue:
            print(i.data,end=' ')

    def isEmpty(self):
        return len(self.queue)<=0

    def getFront(self):
        return self.queue[-1]

    def getLast(self):
        return self.queue[0]

def printOuterTreeLevelWise(root):
    q=Queue()
    q.enqueue(root)
    level=0
    while True:
        if q.isEmpty():
            break
        count=q.size()
        initialcount=count
        level+=1
        if q.size()==1:
            print(q.getFront().data)
        else:
            print(q.getFront().data,q.getLast().data)
        while count>0:
            front=q.getFront()
            if front.left:
                q.enqueue(front.left)
            if front.right:
                q.enqueue(front.right)
            temp=q.dequeue()
            count-=1
           

tree=Tree()
tree.root=Node(15)

tree.root.left=Node(10)
tree.root.right=Node(20)

tree.root.left.left=Node(8)
tree.root.left.right=Node(12)

tree.root.right.left=Node(16)
#tree.root.right.right=Node(25)
        
printOuterTreeLevelWise(tree.root)
