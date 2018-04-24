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

def getith(head,index):
    temp=head
    count=0
    while temp!=None:
        if index==count:
            return temp
        temp=temp.next
        count+=1
        
def length(head):
    temp=head
    count=0
    while temp!=None:
        count+=1
        temp=temp.next
    return count

def swap(head,index1,index2):

    prevnode1=None
    if index1==0:
        pass
        #Do nothing
    else:
        prevnode1=getith(head,index1-1)
    prevnode2=getith(head,index2-1)

    node1=getith(head,index1)
    node2=getith(head,index2)

    if index2==length(head)-1 and index1==0:

        
        temp=node1.next
        node1.next=node2.next
        node2.next=temp

        prevnode2.next=node1
        
        head=node2
        

    elif  index2!=length(head)-1 and index1!=0:

        temp=prevnode1.next
        prevnode1.next=prevnode2.next
        prevnode2.next=temp

        temp=node1.next
        node1.next=node2.next
        node2.next=temp

    elif index1!=None and index2==length(head)-1:

        
        temp=prevnode1.next
        prevnode1.next=prevnode2.next
        prevnode2.next=temp

        node2.next=node1.next
        node1.next=None

    elif index1==0 and index2!=length(head)-1:

        prevnode2.next=node1
        
        temp=node1.next
        node1.next=node2.next
        node2.next=temp
        prevnode2.next=node1
        
        head=node2

    return head        

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)

printList(l.head)

l.head=swap(l.head,2,4)

printList(l.head)
