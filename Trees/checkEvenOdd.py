class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):

    def __init__(self):
        self.head=None

def checkEven(head):
    if head.next==None:
        return False
    if head.next.next==None:
        return True
    if head.next:    
        return checkEven(head.next.next)

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)
l.head.next.next.next.next.next=Node(6)
l.head.next.next.next.next.next.next=Node(7)
print(checkEven(l.head))
