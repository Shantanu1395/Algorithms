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

def isSame(head1,head2):
    if head1==None and head2==None:
        return True
    if head1==None or head2==None:
        return False
    return head1.data==head2.data and isSame(head1.next,head2.next)
l1=LinkedList()
l1.head=Node(1)
l1.head.next=Node(2)
l1.head.next.next=Node(3)
l1.head.next.next.next=Node(4)
l1.head.next.next.next.next=Node(5)
l1.head.next.next.next.next.next=Node(6)

l2=LinkedList()
l2.head=Node(1)
l2.head.next=Node(2)
l2.head.next.next=Node(3)
l2.head.next.next.next=Node(4)
l2.head.next.next.next.next=Node(5)
l2.head.next.next.next.next.next=Node(8)

print(isSame(l1.head,l2.head))
