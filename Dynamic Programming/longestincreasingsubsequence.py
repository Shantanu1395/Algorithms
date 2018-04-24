arr=[10,22,9,33,21,50,41,60]
count=[1]*len(arr)
for i in range(1,len(arr)):
    for j in range(0,i):
        if(arr[i]>arr[j]):
            count[i]=max(count[i],count[j]+1)
print(max(count[len(count)-1]))
