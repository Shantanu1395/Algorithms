import math

class SegmentTree:
    def __init__(self):
        self.st = []
        self.size = 0
    
    def mid(self, start, end):
        return start + (end - start)//2
        
    def constructSegmentTree(self, arr):
        level = int(math.ceil(math.log2(len(arr))))
        height = 2 * (2**level) - 1;
        self.size = height
        self.st = [0]*height
        self.constructSegmentTreeUtil(arr, 0, len(arr)-1, 0)
        
    def constructSegmentTreeUtil(self, arr, start, end, i):
        #Only 1 element is present in array, store it in current node and return
        if start == end:
            self.st[i] = arr[start]
            return arr[start]
        
        #If there are more values recur left and right
        mid = self.mid(start, end)
        self.st[i] = min(self.constructSegmentTreeUtil(arr, start, mid, 2*i + 1), self.constructSegmentTreeUtil(arr, mid + 1, end, 2*i + 2)) 
        return self.st[i]

    def RMQ(self, n, qs, qe): 
        # Check for erroneous input values 
        if (qs < 0 or qe > n - 1 or qs > qe): 
            print("Invalid Input"); 
            return -1; 
  
        return self.RMQUtil(0, n - 1, qs, qe, 0)
    
    
    def RMQUtil(self, ss, se, qs, qe, index): 
        # If segment of this node is a part of given range, then 
        # return the min of the segment 
        if (qs <= ss and qe >= se):
            return self.st[index]; 
  
        # If segment of this node is outside the given range 
        if (se < qs or ss > qe): 
            return 999999999; 
  
        # If a part of this segment overlaps with the given range 
        mid = self.mid(ss, se)
        return min(self.RMQUtil(ss, mid, qs, qe, 2 * index + 1), 
                self.RMQUtil(mid + 1, se, qs, qe, 2 * index + 2)); 

arr = [1, 3, 2, 7, 9, 11]
s = SegmentTree()
s.constructSegmentTree(arr)
print(s.RMQ(len(arr), 0, 4))
