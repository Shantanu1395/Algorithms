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
        return len(self.stack) <= 0
            
    def show(self):
        temp = self.stack[::-1]
        for i in temp:
            print(i.data,end=' ')
        print()    


class Queue():
    def __init__(self):
        self.arr=[]
        self.size=0

    def rightenqueue(self,data):
        self.arr.append(data)
        self.size+=1

    def leftenqueue(self,data):
        self.arr.insert(0,data)
        self.size+=1
        
    def leftdequeue(self):
        temp=self.arr[0]
        del self.arr[0]
        self.size-=1
        return temp

    def rightdequeue(self):
        temp=self.arr[-1]
        del self.arr[-1]
        self.size-=1
        return temp
    
    def isEmpty(self):
        return self.size<=0

    def getSize(self):
        return self.size

    def topleftElement(self):
        return self.arr[0]

    def toprightElement(self):
        return self.arr[-1]

    def display(self):
       for i in self.arr:
            print(i.data,end=' ')
       print()


def spiralOrderTraversal(root):
    q=Queue()
    q.rightenqueue(root)
    level=0
    while True:
        if q.isEmpty():
            break
        count=q.getSize()
        level+=1
        
        while(count>0):
            s=Stack()
            if level%2!=0:
                top=q.toprightElement()
                if top.left:
                    q.leftenqueue(top.left)    
                if top.right:
                    q.leftenqueue(top.right)
                print(q.rightdequeue().data,end=' ')
            else:
                top=q.topleftElement()
                if top.left:
                    s.push(top.left)#q.rightenqueue(top.left)
                if top.right:
                    s.push(top.right)#q.rightenqueue(top.right)
                while not s.isEmpty():
                    q.rightenqueue(s.pop())
                print(q.leftdequeue().data,end=' ')
            count-=1
                
tree=Tree()
tree.root=Node(1)

tree.root.left=Node(3)
tree.root.right=Node(2)

tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

tree.root.right.right.right=Node(8)
tree.root.right.right.left=Node(9)
tree.root.left.right.left=Node(11)
tree.root.left.right.right=Node(10)

tree.root.right.right.left.left=Node(12)
tree.root.right.right.left.right=Node(13)
spiralOrderTraversal(tree.root)
