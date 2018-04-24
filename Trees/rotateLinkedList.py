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

def frontToEnd(head):
    temp=head
    temphead=head
    while temp.next!=None:
        temp=temp.next
    head=head.next    
    temp.next=temphead
    temphead.next=None
    return head

def rotate(head,k):
    for i in range(k):
        head=frontToEnd(head)
    return head    

l=LinkedList()
l.head=Node(10)
l.head.next=Node(20)
l.head.next.next=Node(30)
l.head.next.next.next=Node(40)
l.head.next.next.next.next=Node(50)
l.head.next.next.next.next.next=Node(60)

printList(l.head)
l.head=rotate(l.head,2)
printList(l.head)
