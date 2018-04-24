total,n=map(int,input().split(" "))
coins=list(map(int,input().split(" ")))
arr=[0]*(total+1)
arr[0]=1

for i in range(1,len(coins)+1):
    for j in range(coins[i-1],total+1):
        #print("".join(str(arr)))
        arr[j]=arr[j-coins[i-1]]+arr[j]
    
print(arr[total])        
