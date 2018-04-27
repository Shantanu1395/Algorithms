def binarySearch(arr,x,l,h):
    mid=(l+h)//2
    if l==h:
        return False
    return arr[mid]==x or binarySearch(arr,x,l,mid) or binarySearch(arr,x,mid+1,h)

def bs(arr,x,l,h):
    if l==h:
        return -1

    mid=(l+h)//2

    if arr[mid]==x:
        return x
    
    if arr[mid]>=x:
        return bs(arr,x,l,mid)
    else:
        return bs(arr,x,mid+1,h)
        
arr=[1,2,3,4,5,6,7,8]
print(bs(arr,10,0,len(arr)-1))
