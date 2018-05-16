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

#Assuming even come first and then odd
def repositionOddEven(head):
    curr=head
    previous=head
    while curr!=None:
        if curr.data%2==0 and not curr == head:
            store=curr
            previous.next=curr.next
            curr.next=head
            head=curr
            curr=previous.next
        else:
            previous=curr
            curr=curr.next    
    return head

l1=LinkedList()
l1.head=Node(1)
l1.head.next=Node(2)
l1.head.next.next=Node(3)
l1.head.next.next.next=Node(4)
l1.head.next.next.next.next=Node(5)
l1.head.next.next.next.next.next=Node(6)
l1.head.next.next.next.next.next.next=Node(7)

printList(l1.head)
l1.head=repositionOddEven(l1.head)
printList(l1.head)
