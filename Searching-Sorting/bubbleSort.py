def bubbleSort1(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>=arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp

def bubbleSort2(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]<=arr[j]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp                

arr=[23,52,15,-43,58,97,3]
bubbleSort1(arr)
print(arr)
