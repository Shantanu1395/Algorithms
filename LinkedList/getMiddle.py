class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):

    def __init__(self):
        self.head=None

def middle(head):
    slow=head
    fast=head
    while True:
        if fast.next==None or fast.next.next==None:
            break
        
        if fast.next:
            fast=fast.next.next
            
        slow=slow.next
    print(slow.data)

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)
l.head.next.next.next.next.next=Node(6)
l.head.next.next.next.next.next.next=Node(7)
middle(l.head)
