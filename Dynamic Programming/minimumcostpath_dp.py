def mincost(arr,x,y):
    temp=[[0]*y for i in range(x)]
    temp[0][0]=arr[0][0]
    for i in range(1,x):
        temp[i][0]=arr[i][0]+temp[i-1][0]
    for i in range(1,y):
        temp[0][i]=arr[0][i]+temp[0][i-1]
    for i in range(1,x):
        for j in range(1,y):
            temp[i][j]=arr[i][j]+min(temp[i-1][j],temp[i-1][j-1],temp[i][j-1])
    return temp[x-1][y-1]        
arr=[[1,2,3],[5,8,2],[1,5,3]]
print(mincost(arr,3,3))
