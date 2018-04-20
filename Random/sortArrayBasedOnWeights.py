#Sort Array Based on weights

def sortArray(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j][1]<arr[i][1]:
                temp=arr[j][1]
                arr[j][1]=arr[i][1]
                arr[i][1]=temp

def printArray(arr):
    for i in arr:
        print(i)

arr=[[10,20],[36,10],[89,2]]
sortArray(arr)
printArray(arr)
