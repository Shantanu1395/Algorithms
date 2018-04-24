class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None


def merge(head1,head2):
    temp1=head1
    temp2=head2
    l3=LinkedList()
    temp3=None
    
    while(True):
        if temp1==None and temp2==None:
            break
        if temp1 and temp2:
            if temp1.data>=temp2.data:
                if temp3==None:
                    l3.head=temp2
                    temp3=l3.head
                else:
                    temp3.next=temp2
                    temp3=temp3.next
                temp2=temp2.next
            else:
                if temp3==None:
                    l3.head=temp1
                    temp3=l3.head
                else:
                    temp3.next=temp1
                    temp3=temp3.next
                temp1=temp1.next
                
        if temp1==None:
            if temp3==None:
                    l3.head=temp2
                    temp3=l3.head
            else:       
                temp3.next=temp2
                temp3=temp3.next
            if temp2:
                temp2=temp2.next

        if temp2==None:
            if temp3==None:
                    l3.head=temp1
                    temp3=l3.head
            else:        
                temp3.next=temp1
                temp3=temp3.next
            if temp1:
                temp1=temp1.next
            
    return l3.head        

l1=LinkedList()
l2=LinkedList()
l3=LinkedList()

l1.head=Node(1)
l1.head.next=Node(3)
l1.head.next.next=Node(5)
l1.head.next.next.next=Node(7)

l2.head=Node(2)
l2.head.next=Node(4)
l2.head.next.next=Node(8)
l2.head.next.next.next=Node(10)

l3.head=merge(l1.head,l2.head)

temp=l3.head
while temp!=None:
    if temp.next==None:
        print(temp.data)
    else:    
        print(temp.data,end='->')
    temp=temp.next
