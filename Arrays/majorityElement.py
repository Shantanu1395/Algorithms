from collections import defaultdict
def majorityElement(arr):
    d=defaultdict(int)
    total=-1
    myans=-1
    for i in arr:
        d[i]+=1
        if d[i]>total:
            total=d[i]
            myans=i
    return myans

print(majorityElement([3,3,4,2,4,4,2,4,4,3,3,3,3]))
