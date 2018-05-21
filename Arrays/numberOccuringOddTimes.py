from collections import defaultdict
def numberOccuringOddTimes(arr):
    d=defaultdict(int)
    temp=-1
    for i in arr:
        d[i]+=1
        if d[i]==2:
            d[i]-=1
        if not (d[i]==0):
            temp=i
    return temp

print(numberOccuringOddTimes([1,2,3,2,3,1,3,3]))
