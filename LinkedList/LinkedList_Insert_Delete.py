class Node(object):

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():

    def __init__(self):
        self.head=None

    def insertBegin(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=Node(data)
            temp.next=self.head
            self.head=temp

    def insertEnd(self,data):
        temp=self.head
        if temp==None:
            self.head=Node(data)
        else:
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)    

    def insertAt(self,index,data):
        temp=self.head
        if temp==None:
            self.head=Node(data)
        else:
            count=0
            while count!=index-1:
                temp=temp.next
                count+=1
            node=Node(data)
            node.next=temp.next
            temp.next=node

    def deleteElement(self,key):
        temp=self.head
        if temp==None:
            print("Nothing to delete")
        else:    
            previous=temp
            flag=False
            while temp!=None and temp.data!=key:
                previous=temp
                temp=temp.next
        
            previous.next=temp.next
            temp.next=None
            del temp

    def deleteAtIndex(self,key):
        temp=self.head    
        if temp==None:
            print("Nothing to delete")
        else:    
            previous=temp
            count=0
            while temp!=None or count!=key:
                if count==key:
                    break
                previous=temp
                temp=temp.next
                count+=1
            previous.next=temp.next
            temp.next=None
            del temp
        
    def printList(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next
        print()    

l=LinkedList()
l.deleteElement(20)
l.insertBegin(10)
l.insertBegin(20)
l.insertBegin(30)

l.insertEnd(40)

l.insertAt(4,100)

l.printList()
l.deleteElement(20)
l.printList()
l.deleteElement(100)
l.printList()
l.deleteElement(10)
l.printList()

l.insertBegin(10)
l.insertBegin(20)
l.printList()
l.deleteAtIndex(2)
l.printList()
