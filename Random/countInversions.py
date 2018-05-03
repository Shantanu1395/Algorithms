count=0

def util(arr,low,mid,high):
    global count
    left=arr[low:mid+1]
    right=arr[mid+1:high+1]
    #print(left,right)
    i,j,k=0,0,low
    
    while i<len(left) and j<len(right):
        
        if left[i]<right[j]:
            arr[k]=left[i]
            k+=1
            i+=1

        else:
            arr[k]=right[j]
            count+=(len(left)-i)
            k+=1
            j+=1

    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1
        
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1
        
def countInversions(arr,low,high):
    if low<high:
        mid=(low+high)//2
        countInversions(arr,low,mid)
        countInversions(arr,mid+1,high)
        util(arr,low,mid,high)

arr=[2,4,1,3,5]
arr=[1, 20, 6, 4, 5]
countInversions(arr,0,len(arr)-1)
print(count)
print(arr)
