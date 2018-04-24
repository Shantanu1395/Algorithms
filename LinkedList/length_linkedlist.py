class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

def length_iterative(head):
    l=0
    temp=head
    while temp!=None:
        temp=temp.next
        l+=1
    return l    

def length_recursive(head):
    if head.next==None:
        return 1
    else:
        return length_recursive(head.next)+1
    
l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)

print(length_iterative(l.head))
print(length_recursive(l.head))
