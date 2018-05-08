def sortByFrequency(arr):
    arr.sort()
    count=1
    temp=[]
    print(arr)
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            temp.append([arr[i-1],count])
            count=1
    temp.append((arr[-1],count))        

    for i in range(len(temp)):
        for j in range(i):
            if temp[i][1]<temp[j][1]:
                swap=temp[i]
                temp[i]=temp[j]
                temp[j]=swap
                
    for i in temp:
        for j in range(i[1]):
            print(i[0],end=' ')
            
arr=[2,5,2,8,5,6,8,8]
sortByFrequency(arr)
