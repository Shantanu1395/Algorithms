def maxSize(arr):
    temp=[[1]*len(arr[0]) for i in range(len(arr))]
    m=-1
    indexi=-1
    indexj=-1
    for i in range(len(arr)-1):
        for j in range(len(arr[i])-1):
            if arr[i][j]==1 and ((arr[i][j]==arr[i+1][j]) and (arr[i][j]==arr[i][j+1]) and (arr[i][j]==arr[i+1][j+1])):
                temp[i+1][j+1]=min(temp[i][j],temp[i][j+1],temp[i+1][j])+1
                if temp[i+1][j+1]>m:
                    m=temp[i+1][j+1]
                    indexi=i
                    indexj=j
    print(indexi-m+1,indexj-m+1)
    return m

arr=[[0,1,1,0,1],
     [1,1,0,1,0],
     [0,1,1,1,0],
     [1,1,1,1,0],
     [1,1,1,1,1],
     [0,0,0,0,0]]
print(maxSize(arr))
