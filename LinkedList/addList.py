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


def addList(head1,head2):
    carry=0
    temp1=head1
    temp2=head2
    l3=LinkedList()
    temp=None
    total=0
    while temp1!=None and temp2!=None:
#Case 1        
        if temp1 and temp2:
            total=temp1.data+temp2.data+carry

            #2 cases wether head null or not
            if l3.head==None:
                l3.head=Node(total%10)
                temp=l3.head
            else:
                temp.next=Node(total%10)
                temp=temp.next
                
            #Extracting carry    
            if total<10:
                carry=0
            else:    
                carry=int(str(total)[:-1])

            #Incrementing each pointer    
            temp2=temp2.next
            temp1=temp1.next
            
#Case 2                
        if temp1==None:
            total=temp2.data+carry
            temp.next=Node(total)
            temp=temp.next

            #Extracting carry
            if total<10:
                carry=0
            else:    
                carry=int(str(total)[:-1])
            temp2=temp2.next
#Case 3
        if temp2==None:
            total=temp1.data+carry
            temp.next=Node(total%10)
            temp=temp.next

            #Extracting carry
            if total<10:
                carry=0
            else:    
                carry=int(str(total)[:-1])
            temp1=temp1.next


#Checking at end            
    if carry!=0:
        temp.next=Node(carry)
        temp=temp.next
    temp.next=None
    return l3.head



l1=LinkedList()
l1.head=Node(5)
l1.head.next=Node(7)
l1.head.next.next=Node(9)
l1.head.next.next.next=Node(9)

l2=LinkedList()
l2.head=Node(7)
l2.head.next=Node(1)
l2.head.next.next=Node(9)

l3=LinkedList()
l3.head=addList(l1.head,l2.head)

printList(l1.head)
printList(l2.head)
printList(l3.head)
