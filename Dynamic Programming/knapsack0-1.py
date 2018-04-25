total=7
weight=[1,3,4,5]
val=[1,4,5,7]

arr=[[0 for j in range((total+1))] for i in range(len(weight)+1)]

for i in range(1,len(weight)+1):
    for j in range(1,total+1):
        if j<weight[i-1]:
            arr[i][j]=arr[i-1][j]
        else:
            arr[i][j]=max(arr[i-1][j],arr[i-1][j-weight[i-1]]+val[i-1])

for i in arr:
    print(i)

print(arr[len(weight)][total])
