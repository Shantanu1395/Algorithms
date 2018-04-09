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

def removeDuplicates(head):
    temp=head
    ini=head
    check=temp.next
    while check!=None:
        if ini.data==check.data:
            #printList(head)
            ini.next=check.next
            check.next=None
            check=ini.next
            #printList(head)
        else:
            ini=check
            check=check.next
            #printList(head)        
    return head

l=LinkedList()
l.head=Node(11)
l.head.next=Node(11)
l.head.next.next=Node(11)
l.head.next.next.next=Node(11)
l.head.next.next.next.next=Node(13)
l.head.next.next.next.next.next=Node(13)
l.head.next.next.next.next.next.next=Node(20)
printList(l.head)
l.head=removeDuplicates(l.head)
printList(l.head)

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(3)
l.head.next.next.next.next=Node(4)
l.head.next.next.next.next.next=Node(4)
printList(l.head)
l.head=removeDuplicates(l.head)
printList(l.head)
