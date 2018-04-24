arr=[-2,-3,4,-1,-2,1,5,-3]
sumtillnow=arr[0]
globalsum=arr[0]
for i in range(1,len(arr)):
    sumtillnow=max(arr[i]+sumtillnow,arr[i])
    globalsum=max(globalsum,sumtillnow)
    #print(arr[i]+sumtillnow,arr[i],globalsum,sumtillnow)
print(globalsum)        
