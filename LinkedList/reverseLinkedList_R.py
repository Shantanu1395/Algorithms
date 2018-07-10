class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self,head = None):
        self.head = head
        
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end = ' ')
            temp = temp.next

def reverse(head):
    temp = head
    prev = None
    while temp != None:
        store = temp.next
        temp.next = prev
        prev = temp
        temp = store
        
    head = prev
    return head


l1 = LinkedList()
l1.head = Node(1)
l1.head.next = Node(2)
l1.head.next.next = Node(3)
l1.head.next.next.next = Node(4)
l1.head.next.next.next.next = Node(5)
l1.head = reverse(l1.head)
l1.display()
