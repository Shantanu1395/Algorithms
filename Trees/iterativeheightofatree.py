class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

class Queue():
    def __init__(self):
        self.arr=[]
        self.size=0

    def enqueue(self,data):
        self.arr.append(data)
        self.size+=1
        
    def dequeue(self):
        del self.arr[0]
        self.size-=1
        
    def isEmpty(self):
        return self.size<=0

    def getSize(self):
        return self.size

    def topele(self):
        return self.arr[0]

    def display(self):
       for i in self.arr:
            print(i.data,end=' ')
       print()
        
def calHeight(root):
    temp=root
    q=Queue()
    q.enqueue(temp)
    treeHeight=0
    while True:
        if q.isEmpty():
            break
        count=q.getSize()
        treeHeight+=1
        while(count>0):
            top=q.topele()
            if top.left:
                q.enqueue(top.left)
            if top.right:
                q.enqueue(top.right)
            count-=1    
            q.dequeue()    
                
    return treeHeight       

tree=Tree()

tree.root=Node(1)

tree.root.right=Node(2)
tree.root.left=Node(3)

tree.root.right.left=Node(4)
tree.root.right.right=Node(5)

tree.root.right.right.left=Node(8)

print(calHeight(tree.root))
