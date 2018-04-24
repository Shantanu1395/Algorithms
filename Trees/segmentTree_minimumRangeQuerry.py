class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def  __init__(self):
        self.root=None


def buildSegmentTree(arr,tree,low,high,node):
    mid=(low+high)//2
    if low==high:
        tree[node]=arr[low]
        return
    buildSegmentTree(arr,tree,low,mid,node*2)
    buildSegmentTree(arr,tree,mid+1,high,node*2+1)
    tree[node]=min(tree[node*2],tree[node*2+1])
    
def findMinimum(tree,checklow,checkhigh,low,high,index):
    if checkhigh<low or high<checklow:
        return 99999
    if low<=checklow and checkhigh<=high:
        return tree[index]
    return min(findMinimum(tree,l,h,low,high,index*2),findMinimum(tree,l,h,low,high,index*2+1))

arr=[-1,3,4,0,2,1]
tree=[0]*(len(arr)*2+1)

buildSegmentTree(arr,tree,2,4,1)            #O(n)
print(findMinimum(tree,2,4,0,len(arr)-1,1)) #O(log(n))
