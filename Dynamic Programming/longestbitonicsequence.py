#s=list(map(int,input().strip().split(" ")))
s=[2,-1,4,3,5,-1,3,2]
#s=[1,11,2,10,4,5,2,1]
arr1=[1]*len(s)
arr2=[1]*len(s)
for i in range(1,len(s)):
    for j in range(i):
        if s[i]>s[j]:
            arr1[i]=max(arr1[i],arr1[j]+1)

for i in range(len(s)-2,-1,-1):
    for j in range(len(s)-1,i,-1):
        if s[i]>=s[j]:
            arr2[i]=max(arr2[i],arr2[j]+1)

m=-999999            
for i,j in zip(arr1,arr2):
    m=max(m,i+j-1)
print(m)      
