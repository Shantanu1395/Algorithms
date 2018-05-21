def findMissingNumber(arr):
    n=len(arr)
    n+=1
    total=n*(n+1)//2
    for i in arr:
        total-=i
    return total

###TBR
def findMissingNumberXor(arr):
    x1=arr[0]
    x2=1
    for i in range(1,len(arr)):
       x1=arr[i]^x1
    for i in range(2,len(arr)+2):   
        x2=x2^i
    return x1^x2

arr=[1,2,4,5,6]
print(findMissingNumberXor(arr))
