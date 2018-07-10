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
    
    def front(self):
        return self.queue[-1]
    
def levelOrder(root):
    q=Queue()
    q.enqueue(root)
    while not q.isEmpty():
        count = q.size()
        arr=[]
        while count > 0:
            front = q.front()
            if front.left:
                q.enqueue(front.left)
            if front.right:
                q.enqueue(front.right)
            print(str(q.dequeue().data),end=" ")
            count-=1
        print()    

def insert(root,data):
    parent = root
    curr = root
    while True:
        if curr.data>=data:
            parent=curr
            curr=curr.left
            if curr == None:
                parent.left=Node(data)
                break
        else:
            parent = curr
            curr = curr.right
            
            if curr == None:
                parent.right=Node(data)
                break
    return root        
                

def inorder(root):
    if not root == None:
        inorder(root.left)
        print(str(root.data)+" ")
        inorder(root.right)
   
tree=Tree()
tree.root=Node(10)
tree.root=insert(tree.root,8)
tree.root=insert(tree.root,12)
tree.root=insert(tree.root,3)
tree.root=insert(tree.root,2)
tree.root=insert(tree.root,11)


levelOrder(tree.root)

