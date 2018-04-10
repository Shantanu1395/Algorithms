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

def multiply2NumbersAsLinkedList(head1,head2):
    num1,num2=0,0
    temp1,temp2=head1,head2
    while temp1!=None:
                
        num1=(temp1.data+num1)*10
        temp1=temp1.next
    while temp2!=None:
        num2=(temp2.data+num2)*10
        temp2=temp2.next
    return num1//10*num2//10    
        

l1=LinkedList()
l1.head=Node(3)
l1.head.next=Node(2)
l1.head.next.next=Node(1)

l2=LinkedList()
l2.head=Node(1)
l2.head.next=Node(2)

print(multiply2NumbersAsLinkedList(l1.head,l2.head))
