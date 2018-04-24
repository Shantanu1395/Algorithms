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

def isPallindrome(head):
    temp=head
    s=""
    while temp!=None:
        s+=temp.data
        temp=temp.next 
    return s==s[::-1]

l1=LinkedList()
l1.head=Node('a')
l1.head.next=Node('bc')
l1.head.next.next=Node('d')
l1.head.next.next.next=Node('d')
l1.head.next.next.next.next=Node('dcb')
l1.head.next.next.next.next.next=Node('a')
print(isPallindrome(l1.head))
