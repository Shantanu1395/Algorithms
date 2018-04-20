arr=[0,1,2,3,4,5,6,7]
arr=[3,6,4,1,2,5]

largestI=-1
for i in range(0,len(arr)-1):
    if arr[i]<arr[i+1]:
        largestI=i

if(largestI==-1):
    print("No element found")

largestJ=-1
for i in range(0,len(arr)):
    if arr[largestI]<arr[i]:
        largestJ=i

arr[largestI],arr[largestJ]=arr[largestJ],arr[largestI]

temp=arr[largestI+1:len(arr)]
temp=temp[::-1]
arr[largestI+1:len(arr)]=temp

print(arr)
