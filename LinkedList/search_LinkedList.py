class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

def search_Recursive(head,element):
    if head==None:
        return False
    return head.data==element or searchRecursive(head.next,element) 

def search_Iterative(head,element):
    temp=head
    while temp!=None:
        if temp.data==element:
            return True
        temp=temp.next
    return False

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)

print(search_Iterative(l.head,10))
print(search_Recursive(l.head,3))
