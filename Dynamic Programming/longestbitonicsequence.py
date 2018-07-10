"""
Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic if it is first increasing, then decreasing.
Write a function that takes an array as argument and returns the length of the longest bitonic subsequence.

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)


"""

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
