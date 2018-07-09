"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.

LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def lcs(s1,s2):
    ls1,ls2=len(s1),len(s2)
    
    l=[[0 for j in range(ls2+1)] for i in range(ls1+1)]
        
    for i in range(1,ls1+1):
        for j in range(1,ls2+1):
            if(s1[i-1]==s2[j-1]):
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i][j-1],l[i-1][j])
    return l[ls1][ls2]
        
        
s1=input()
s2=input()
print(lcs(s1,s2))
