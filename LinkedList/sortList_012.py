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

def printList(head):
    temp=head
    while temp!=None:
        print(temp.data,end=' ')
        temp=temp.next
    print()    

def count0(head):
    temp=head
    count=0
    while temp!=None:
        if temp.data==0:
            count+=1
        temp=temp.next
    return count

def sortList(head):
    temp=head
    count=length(head)
    c=0
    previous=temp
    while c<count-count0(head)-1:
        #print("Iteration:"+str(c))
        #print("Temp.data:"+str(temp.data))
        if temp.data==2:
            if c==0:
                #print("Iteration:"+str(c))
                #printList(head)
                store=temp
                head=head.next
                #printList(head)
                store.next=None
                temp=head
                previous=None
                tmp=head
                while tmp.next!=None:
                    tmp=tmp.next
                tmp.next=store
                #printList(head)
            else:
                #print("Iteration:"+str(c))
                store=temp
                tmp=temp.next
                previous.next=temp.next
                store.next=None
                temp=tmp
                while tmp.next!=None:
                    tmp=tmp.next
                tmp.next=store
                
        if temp.data==0 and c>0:
            #print(previous.data,temp.data,temp.next.data)
            store=temp
            tmp=temp.next
            previous.next=temp.next
            store.next=head
            head=store
            temp=tmp
            #printList(head)    
        c+=1
        previous=temp
        temp=temp.next
    return head    
                
                
            

l=LinkedList()
l.head=Node(2)
l.head.next=Node(1)
l.head.next.next=Node(2)
l.head.next.next.next=Node(1)
l.head.next.next.next.next=Node(0)
l.head.next.next.next.next.next=Node(1)
l.head.next.next.next.next.next.next=Node(0)
l.head.next.next.next.next.next.next.next=Node(1)
l.head.next.next.next.next.next.next.next.next=Node(2)
printList(l.head)
l.head=sortList(l.head)
printList(l.head)
