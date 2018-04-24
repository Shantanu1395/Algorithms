class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

def length(head):
    temp=head
    count=0
    while temp!=None:   
        count+=1
        temp=temp.next
    return count

def printList(head):
    temp=head
    while temp!=None:
        print(temp.data,end=' ')
        temp=temp.next
    print()    

def LastToFront(head):
    temp=head
    previous=None
    while temp.next!=None:
        previous=temp
        temp=temp.next
    temp.next=head
    previous.next=None
    head=temp
    return head

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)
l.head.next.next.next.next.next=Node(6)
l.head.next.next.next.next.next.next=Node(7)
printList(l.head)
l.head=LastToFront(l.head)
printList(l.head)
