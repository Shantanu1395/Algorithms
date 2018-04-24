class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

def length(head):
    temp=head
    count=0
    while temp!=None:   
        count+=1
        temp=temp.next
    return count

def printList(head):
    temp=head
    while temp!=None:
        print(temp.data,end=' ')
        temp=temp.next
    print()    

def insertListAtKthPoistion(head1,head2,k):
    temp1=head1
    count=0
    assert k<=length(head1)
    while count<k-1:
        count+=1
        temp1=temp1.next

    temp2=head2
    while temp2.next!=None:
        temp2=temp2.next

    if k==0:
        temp2.next=head1
        head1=head2
    else:    
        temp2.next=temp1.next
        temp1.next=head2
    return head1    

l1=LinkedList()
l1.head=Node(1)
l1.head.next=Node(2)
l1.head.next.next=Node(3)
l1.head.next.next.next=Node(4)
l1.head.next.next.next.next=Node(5)
l1.head.next.next.next.next.next=Node(6)
l1.head.next.next.next.next.next.next=Node(7)
l1.head.next.next.next.next.next.next.next=Node(8)
l1.head.next.next.next.next.next.next.next.next=Node(9)

l2=LinkedList()
l2.head=Node(10)
l2.head.next=Node(20)
l2.head.next.next=Node(30)
l2.head.next.next.next=Node(40)
l2.head.next.next.next.next=Node(50)
l2.head.next.next.next.next.next=Node(60)
l2.head.next.next.next.next.next.next=Node(70)

l1.head=insertListAtKthPoistion(l1.head,l2.head,9)
printList(l1.head)
