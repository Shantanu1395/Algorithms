class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.head=None

    def insert(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            curr1=self.head
            while(curr1!=None):
                if(curr1.left==None and data<curr1.data):
                    curr1.left=temp
                    break
                if(curr1.right==None and data>=curr1.data):
                    curr1.right=temp
                    break
                if(data<curr1.data):
                    curr1=curr1.left
                else:
                    curr1=curr1.right

    @staticmethod                
    def preot(h):
        if h==None:
            return 
        print(h.data,end=' ')
        Tree.preot(h.left)
        Tree.preot(h.right)

    @staticmethod                
    def postot(h):
        if h==None:
            return 
        Tree.postot(h.left)
        Tree.postot(h.right)
        print(h.data,end=' ')
        
    @staticmethod                
    def inot(h):
        if h==None:
            return 
        Tree.inot(h.left)
        print(h.data,end=' ')
        Tree.inot(h.right)

    @staticmethod                
    def levelorder(h):
        arr=[]
        arr.append(h)
        while len(arr)>0:
            if(arr[0].left!=None):
                arr.append(arr[0].left)
            if(arr[0].right!=None):
                arr.append(arr[0].right)
            print(arr[0].data,end=' ')
            del arr[0]
            
    @staticmethod                
    def reverselevelorder(h):
        arr=[]
        arr.append(h)
        stk=[]
        while len(arr)>0:
            if(arr[0].right!=None):
                arr.append(arr[0].right)
            if(arr[0].left!=None):
                arr.append(arr[0].left)
            
            stk.append(arr[0].data)
            del arr[0]        
        print(" ".join(map(str,stk[::-1])))

        
tree=Tree()
tree.insert(10)
tree.insert(3)
tree.insert(15)
tree.insert(1)
tree.insert(5)
tree.insert(2)
tree.insert(13) 
tree.preot(tree.head)
print()
tree.inot(tree.head)
print()
tree.postot(tree.head)
print()
tree.levelorder(tree.head)        
print()
tree.reverselevelorder(tree.head)
