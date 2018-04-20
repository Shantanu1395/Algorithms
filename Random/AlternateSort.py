#Alternate Sort
arr=[1, 2, 3, 4, 5, 6, 7]
arr.sort()

newarr=[0]*len(arr)

k1=0
for i in range(len(arr)):
    if i%2==1:
        newarr[i]=arr[k1]
        k1+=1

for i in range(len(arr)-1,-1,-1):
    if i%2==0:
        newarr[i]=arr[k1]
        k1+=1        
        
print(newarr)        
