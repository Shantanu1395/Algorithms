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

def firstNonRepeatingElement(head):
    temp=head
    repeating=[]
    while temp.next!=None:
        tempnext=temp.next
        flag=False
        while tempnext!=None:
            if temp.data==tempnext.data:
                repeating.append(temp.data)
            tempnext=tempnext.next
        
        if temp.data not in repeating:
            return temp.data
        temp=temp.next
    return None    
    
l1=LinkedList()
l1.head=Node(10)
l1.head.next=Node(20)
l1.head.next.next=Node(30)
l1.head.next.next.next=Node(10)
l1.head.next.next.next.next=Node(20)
l1.head.next.next.next.next.next=Node(40)
l1.head.next.next.next.next.next.next=Node(30)

l2=LinkedList()
l2.head=Node(1)
l2.head.next=Node(1)
l2.head.next.next=Node(2)
l2.head.next.next.next=Node(2)
l2.head.next.next.next.next=Node(3)
l2.head.next.next.next.next.next=Node(4)
l2.head.next.next.next.next.next.next=Node(3)
l2.head.next.next.next.next.next.next.next=Node(4)


print(firstNonRepeatingElement(l1.head))
print(firstNonRepeatingElement(l2.head))
