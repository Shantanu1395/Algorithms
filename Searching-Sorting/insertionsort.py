#Properties
#1.Stable
#2.Inplace
#3.Better than selection sort and bubble sort
#4.Good for small arrays(length<25)/almost sorted arrays

#By swapping each element
def insertionSort1(arr):
    i=1
    while i<len(arr):
        j=i-1
        storedi=i
        while j>=0:
            if arr[storedi]<arr[j]:
                temp=arr[storedi]
                arr[storedi]=arr[j]
                arr[j]=temp
                storedi=j
            j-=1
        i+=1

#By shifting the elements
def insertionSort2(arr):
    i=1
    while i<len(arr):
        val=arr[i]
        stored=i
        while stored>0 and arr[stored-1]>val:
            arr[stored]=arr[stored-1]
            stored-=1
        arr[stored]=val
        i+=1
        
    
    
arr=[7,8,5,2,4,6,3,-3,26,64]
insertionSort1(arr)
print(arr)

arr=[7,8,5,2,4,6,3,-3,26,64]

insertionSort2(arr)
print(arr)
