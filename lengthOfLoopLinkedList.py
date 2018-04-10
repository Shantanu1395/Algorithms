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

#When loop is definately present
def loopLength_1(head):
    outertemp=head
    while outertemp!=None:
        temp=outertemp
        stored=temp
        flag=True
        count=1
        while temp.next!=stored:
            if count>100:
                flag=False
                break;
            count+=1
            temp=temp.next
        if flag==True:
            return count
        outertemp=outertemp.next    
    return None

#When loop is definately present
def loopLength(head):
    slow=head
    fast=head
    count=0
    flag=False
    while slow!=None:
        if flag and slow==fast:
            return count
        if slow==fast:
            flag=True
        slow=slow.next
        fast=fast.next.next
        count+=1    
    return None

l1=LinkedList()
l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.head.next.next.next=Node(10)
l1.head.next.next.next.next=Node(20)
l1.head.next.next.next.next.next=Node(40)
l1.head.next.next.next.next.next.next=l1.head.next

print(loopLength(l1.head))

