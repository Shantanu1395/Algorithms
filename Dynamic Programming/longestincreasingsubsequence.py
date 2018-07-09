"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
"""

arr=[10,22,9,33,21,50,41,60]
c=[1]*len(arr)
for i in range(1,len(arr)):
    for j in range(0,i):
        if(arr[i]>arr[j]):
            c[i]=max(c[i],c[j]+1)
            
print(max(c))
        
