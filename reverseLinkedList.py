class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):

    def __init__(self,head=None):
        self.head=head

    def reverse(self,curr):
        if curr==None:
            return None

        if curr.next==None:
            self.head=curr
            return
    
        self.reverse(curr.next)
        curr.next.next=curr
        curr.next=None

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=' ')
            temp=temp.next


l1=LinkedList()
l1.head=Node(1)
l1.head.next=Node(2)
l1.head.next.next=Node(3)
l1.head.next.next.next=Node(4)
l1.head.next.next.next.next=Node(5)
l1.reverse(l1.head)
l1.display()
