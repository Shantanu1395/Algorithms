total=13
coins=[7,2,3,6]

arr=[999999]*(total+1)
arr[0]=0

for i in range(len(coins)):
    for j in range(coins[i],total+1):
        arr[j]=min(arr[j-coins[i]]+1,arr[j])
#print(" ".join(str(arr)))
print(arr[len(arr)-1])
