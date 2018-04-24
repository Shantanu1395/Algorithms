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

def printList(head):
    temp=head
    while temp!=None:   
        print(temp.data,end=' ')
        temp=temp.next
    print()    

def sortAbsolutelySortedLinkedList(head):
    curr=head
    check=head.next
    previousCheck=head
    while curr.next!=None:
        #previousCheck=curr
        #check=curr.next
        if check.data<curr.data:
            curr.next=check.next
            check.next=head
            head=check
            check=curr.next
        else:
            check=check.next
            curr=curr.next
    return head         
            
l1=LinkedList()
l1.head=Node(0)
l1.head.next=Node(1)
l1.head.next.next=Node(-2)
l1.head.next.next.next=Node(3)
l1.head.next.next.next.next=Node(4)
l1.head.next.next.next.next.next=Node(5)
l1.head.next.next.next.next.next.next=Node(-5)

printList(l1.head)
l1.head=sortAbsolutelySortedLinkedList(l1.head)
printList(l1.head)
