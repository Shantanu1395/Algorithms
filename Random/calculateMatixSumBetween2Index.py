#Calculate sum in a matrix from one index to another

def calculateSum(arr,x1,y1,x2,y2):
    s=0
    flag=False
    for i in range(len(arr)):
        for j in range(len(arr[i])):

            if i==x2 and j==y2:
                s+=arr[i][j]
                break
            
            if i==x1 and j==y1:
                flag=True

            if flag==True:
                s+=arr[i][j]
    return s                

arr=[
    [1, 2, 3, 4, 6],
    [5, 3, 8, 1, 2],
    [4, 6, 7, 5, 5],
    [2, 4, 8, 9, 4]
    ]

print(calculateSum(arr,2,0,3,4))
