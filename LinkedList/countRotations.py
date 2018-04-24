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

def countRotations(head):
    count=0
    currnode=head
    nextnode=head.next
    while nextnode!=None:
        if nextnode.data<currnode.data:
            count+=1
        currnode=currnode.next
        nextnode=nextnode.next
    return count

l1=LinkedList()
l1.head=Node(6)
l1.head.next=Node(5)
l1.head.next.next=Node(1)
l1.head.next.next.next=Node(2)
l1.head.next.next.next.next=Node(3)
l1.head.next.next.next.next.next=Node(4)
print(countRotations(l1.head))
