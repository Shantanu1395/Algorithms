class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

def detectLoop(head):
    slow=head
    fast=head
    while True:
        #print(slow.data,fast.data)
        slow=slow.next
        if fast.next!=None:
            fast=fast.next.next
        if fast==None or slow==None:
            return False
        if fast==slow:
            return True    
    return False    

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)
l.head.next.next.next.next.next=l.head.next

print(detectLoop(l.head))
