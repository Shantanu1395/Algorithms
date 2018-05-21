def minimumDist(arr,x,y):
    maxrange=9999
    for i in range(len(arr)):
        flag=False
        count=1
        
        if arr[i]==x:
            flag=True
            tocheck=y  
        elif arr[i]==y:
            flag=True
            tocheck=x
        for j in range(i+1,len(arr)):
                
            if arr[j]==tocheck:
                if flag==True:
                    flag=False
                    maxrange=min(maxrange,count)
                    count=1
                    
            if flag==True:
                count+=1
        
    return maxrange

def minDist(arr,x,y):
    temp=-1
    minDistance=9999
    for i in range(len(arr)):
        if arr[i]==x or arr[i]==y:
           temp=i
           break
    for i in range(temp,len(arr)):
        if arr[i]==x or arr[i]==y:
            if not(arr[temp]==arr[i]) and (i-temp)<minDistance:
                minDistance=i-temp
                temp=i
            else:
                temp=i
    return minDistance            

arr=[3,5,4,2,6,5,6,6,5,4,8,3]
x,y=3,6

arr=[2,5,3,5,4,4,2,3]
x,y=3,2

arr=[3,4,5]
x,y=3,5

arr=[1,2]
x,y=1,2

print(minimumDist(arr,x,y))           
print(minDist(arr,x,y))
