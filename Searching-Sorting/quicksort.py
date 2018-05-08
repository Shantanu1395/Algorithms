#Features-
#1.Inplace
#2.Not stable
#3.T(n)=2T(n/2)+O(n)   O(nlog(n))
#Worst-case  O(n^2)

def partition(arr,low,high):
    pivot=arr[high]
    i=low
    for j in range(low,high):
        if arr[j]<=pivot:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i=i+1
            
            
    temp=arr[high]
    arr[high]=arr[i]
    arr[i]=temp
    
    return i

def quicksort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

arr=[32,14,51,61,13,-4,76,43]
quicksort(arr,0,len(arr)-1)
print(arr)
