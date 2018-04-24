class Node(object):
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):

    def __init__(self,head=None):
        self.head=head

def check(head1,head2):
    if head1==None and head2==None:
        return True
    return head1.data==head2.data and head1!=None and head2!=None and check(head1.next,head2.next)

l1=LinkedList()
l1.head=Node('a')
l1.head.next=Node('p')
l1.head.next.next=Node('p')
l1.head.next.next.next=Node('l')
l1.head.next.next.next.next=Node('e')

l2=LinkedList()
l2.head=Node('a')
l2.head.next=Node('p')
l2.head.next.next=Node('p')
l2.head.next.next.next=Node('l')
l2.head.next.next.next.next=Node('e')

print(check(l1.head,l2.head))
