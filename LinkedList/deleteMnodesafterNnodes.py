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

def deleteMnodesAfterNnodes(head,M,N):
    temp=head
    count=1
    while count<N:
        temp=temp.next
        count+=1
    store1=temp
    count=0
    while count<M:
        temp=temp.next
        count+=1
    store2=temp
    store1.next=store2.next
    store2.next=None


l1=LinkedList()
l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.head.next.next.next=Node(40)
l1.head.next.next.next.next=Node(50)
l1.head.next.next.next.next.next=Node(60)
l1.head.next.next.next.next.next.next=Node(70)

printList(l1.head)
deleteMnodesAfterNnodes(l1.head,2,2)
printList(l1.head)
