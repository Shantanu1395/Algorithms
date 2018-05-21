def union(arr1,arr2):
    arr=[]
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            arr.append(arr2[j])
            j+=1
        else:
            arr.append(arr1[i])
            i+=1
            j+=1
            
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    return arr

def intersection(arr1,arr2):
    arr=[]
    i,j=0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            arr.append(arr1[i])
            i+=1
            j+=1
            
    return arr

arr1=[1,3,4,5,7]
arr2=[2,3,5,6]
arr=union(arr1,arr2)
print(arr)
arr=intersection(arr1,arr2)
print(arr)
