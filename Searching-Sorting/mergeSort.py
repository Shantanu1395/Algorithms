def merge(arr,l,m,r):
    left=arr[l:m+1]
    right=arr[m+1:r+1]
    
    i,j,k=0,0,l
    #print(left,right)
    
    while i<len(left) and j<len(right):
        if right[j]<left[i]:
            arr[k]=right[j]
            k+=1
            j+=1
        else:
            arr[k]=left[i]
            k+=1
            i+=1
                    
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1
    #print(arr[l:r])    
    
            

def mergeSort(arr,l,r):
    if l<r:
        mid=(l+(r-1))//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)
        

arr=[45,43,25,64,22,63,7,76,65,43,24,27,82,0]
mergeSort(arr,0,len(arr)-1)
print(arr)
