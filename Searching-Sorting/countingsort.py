def countingSort(arr):
    high=max(arr)
    count=[0]*(high+1)
    
    for i in arr:
        count[i]+=1
        
    for i in range(1,high+1):
        count[i]=count[i]+count[i-1]

    newarr=[0]*(len(arr)+1)
    
    for i in range(len(arr)):
        newarr[count[arr[i]]]=arr[i]
        count[arr[i]]-=1

    arr[:]=newarr[1:]    

arr=[1,4,1,2,7,5,2]
countingSort(arr)
print(arr)
