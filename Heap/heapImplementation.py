class MaxHeap:
    def __init__(self,items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__heapifyUp(len(self.heap)-1)

    
    def push(self, data):
        self.heap.append(data)
        self.__heapifyUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) -1)
            maximum = self.heap.pop()
            self.__heapifyDown(1)
        elif len(self.heap) == 2:
            maximum = self.heap.pop()
        else:
            maximum=False
        return maximum

    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __heapifyUp(self,index):
        parent = index//2  
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index,parent)
            self.__heapifyUp(parent) 

    def __heapifyDown(self,index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__heapifyDown(largest)

    def __str__(self):
        return str(m.heap[0:len(m.heap)])

    def __add__(self,data):
        self.heap.append(data)
        self.__heapifyUp(len(self.heap)-1)
        return self
    

    def heapsort(self):
        i = len(self.heap)-1
        
        while i>1:
            i = len(self.heap)-1
            print(self.pop(),end=' ')
            

m = MaxHeap([95,3,21])
m = m + 105
m = m + 20
print(m)
print(str(m.pop()))
print(str(m.pop()))
print(str(m.pop()))
m.push(10)
m.push(-34)
m.push(95)
print(m)
m.heapsort()

