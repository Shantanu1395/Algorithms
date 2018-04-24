class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

def printReverse_Recursive(head):
    if head!=None:
        printReverse(head.next)
        print(head.data,end=' ')

def printReverse_Iterative(head):
    temp=head
    s=[]
    while temp!=None:
        s.append(temp.data)
        temp=temp.next
    print(s[::-1])    

l=LinkedList()
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)

printReverse_Iterative(l.head)
