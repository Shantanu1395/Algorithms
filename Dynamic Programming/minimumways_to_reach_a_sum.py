total=20
ways=[3,5,10]
arr=[0]*(total+1)
arr[0]=1
for i in arr:
    print(i,end=" ")
print()    
for i in range(len(ways)):
    for j in range(total+1):
        if(ways[i]<=j):
            arr[j]=arr[j-ways[i]]+arr[j]
    for i in arr:
        print(i,end=" ")
    print()    

print(arr[total])  
