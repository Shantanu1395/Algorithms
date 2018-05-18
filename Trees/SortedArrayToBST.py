# Final Tree
#           3
#          / \
#         1   4
#        / \    
#       2   5   
           
class Node():

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():

    def __init__(self):
        self.root=None

def arraytoBST(arr,low,high):
    if low<=high:
        mid=(low+high)//2 
        root=Node(arr[mid])  #Previously Mistaken
        l=arraytoBST(arr,low,mid-1)
        r=arraytoBST(arr,mid+1,high)
        root.left=l
        root.right=r
        return root
    else:
        return None

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

arr=[1,2,3,4,5]
tree=Tree()
tree.root=arraytoBST(arr,0,len(arr)-1)
levelOrder(tree.root)
