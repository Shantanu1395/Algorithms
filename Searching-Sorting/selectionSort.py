def selectionSort(arr):
    for i in range(len(arr)-1):

        store=i
        #Selecting minimum element in remaining array
        for j in range(i+1,len(arr)):
            if arr[j]<=arr[store]:
                store=j
        
        #Swapping with minimum element        
        temp=arr[store]
        arr[store]=arr[i]
        arr[i]=temp
        #print(arr)

arr=[12,42,63,1,53,87,67,54]
print(arr)
selectionSort(arr)
print(arr)
