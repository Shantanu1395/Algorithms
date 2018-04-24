class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

def printList(head):
    temp=head
    while temp!=None:
        print(temp.data,end=' ')
        temp=temp.next
    print()

def length(head):
    temp=head
    count=0
    while temp!=None:   
        count+=1
        temp=temp.next
    return count

def printAlternateNodes(head):
    if head==None:
        return
    print(head.data,end=' ')
    if head.next:
        printAlternateNodes(head.next.next)

#Printing Odd Nodes        
l1=LinkedList()
l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.head.next.next.next=Node(40)
l1.head.next.next.next.next=Node(50)
l1.head.next.next.next.next.next=Node(60)
l1.head.next.next.next.next.next.next=Node(70)

printList(l1.head)
printAlternateNodes(l1.head)

