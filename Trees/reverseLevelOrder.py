class Node(object):

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.isEmpty():
            raise Exception("nothing to pop")
        return self.stack.pop(len(self.stack)-1)
    def peek(self):
        if self.isEmpty():
            raise Exception("Nothing to peek")
        return self.stack[len(self.stack)-1]
    def __sizeOf__(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0
            
    def show(self):
        temp = self.stack[::-1]
        for i in temp:
            print(i.data,end=' ')
        print()    



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


def reverseLevelOrder(root):
    q=Queue()
    q.enqueue(root)
    s=Stack()
    while not q.isEmpty():
        temp=q.dequeue()
        s.push(temp)
        if temp.right:
            q.enqueue(temp.right)
        if temp.left:
            q.enqueue(temp.left)
    s.show()        
                
tree=Tree()
tree.root=Node(1)

tree.root.left=Node(-1)
tree.root.right=Node(11)

tree.root.left.left=Node(-2)
tree.root.left.right=Node(-3)
tree.root.right.left=Node(21)
tree.root.right.right=Node(6)

tree.root.left.right.right=Node(5)

reverseLevelOrder(tree.root)
