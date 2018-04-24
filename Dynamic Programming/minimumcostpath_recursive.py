def mincost(arr,i,j,x,y):
    print(i,j)
    if i>x-1 or j>y-1:
        return 99999
    if i==x-1 and j==y-1:
        return arr[i][j]
    return arr[i][j]+min(mincost(arr,i+1,j,x,y),mincost(arr,i,j+1,x,y),mincost(arr,i+1,j+1,x,y))

arr=[[1,2,3],[5,8,2],[1,5,3]]
print(mincost(arr,0,0,3,3))
