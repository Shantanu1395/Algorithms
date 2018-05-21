def leaders(arr):
    count=1
    small=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>small:
            count+=1
            small=arr[i]
    return count        

arr=[16,17,4,3,5,2]
print(leaders(arr))
