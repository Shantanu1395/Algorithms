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
        temp = self.stack
        for i in temp:
            print(i.data,end=' ')
        print()    


def iterativePreOrder(root):
    s=Stack()
    s.push(root)
    while(not s.isEmpty()):
        temp=s.pop()
        print(temp.data,end=' ')

        if(temp.right):
            s.push(temp.right)
        if(temp.left):
            s.push(temp.left)
            
                
tree=Tree()
tree.root=Node(1)

tree.root.left=Node(-1)
tree.root.right=Node(11)

tree.root.left.left=Node(-2)
tree.root.left.right=Node(-3)
tree.root.right.left=Node(21)
tree.root.right.right=Node(6)

tree.root.left.right.right=Node(5)

iterativePreOrder(tree.root)
