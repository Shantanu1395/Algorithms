def insertionsort(arr):
    i=1
    while i<len(arr):
        val=arr[i]
        stored=i
        while stored>0 and arr[stored-1]>val:
            arr[stored]=arr[stored-1]
            stored-=1
        arr[stored]=val
        i+=1
        


def bucketSort(arr):
    temp=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    for i in range(len(arr)):
        if arr[i]>=0 and arr[i]<10:
            temp[0].append(arr[i])
        if arr[i]>=10 and arr[i]<20:
            temp[1].append(arr[i])
        if arr[i]>=20 and arr[i]<30:
            temp[2].append(arr[i])
        if arr[i]>=30 and arr[i]<40:
            temp[3].append(arr[i])
        if arr[i]>=40 and arr[i]<50:
            temp[4].append(arr[i])    
        if arr[i]>=50 and arr[i]<60:
            temp[5].append(arr[i])
        if arr[i]>=60 and arr[i]<70:
            temp[6].append(arr[i])
        if arr[i]>=70 and arr[i]<80:
            temp[7].append(arr[i])
        if arr[i]>=80 and arr[i]<90:
            temp[8].append(arr[i])
        if arr[i]>=90 and arr[i]<100:
            temp[9].append(arr[i])
            
    final=[]        
    for i in temp:
        insertionsort(i)
        final.extend(i[1:])
    arr[:]=final[:]        
    
arr=[17,13,19,26,21,33,39,31,47,43,41,59,51,67,62,79,4,32,98,87,71,93]
bucketSort(arr)
print(arr)
