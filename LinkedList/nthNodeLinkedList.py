class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

def getNthNode(head,n):
    temp=head
    count=0
    while count!=n:
        count+=1
        temp=temp.next
    return temp.data    

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)
l.head.next.next.next.next.next=l.head.next

print(getNthNode(l.head,3))
