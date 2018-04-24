def lcs(s1,s2):
    ls1,ls2=len(s1),len(s2)
    
    l=[[0 for j in range(ls2+1)] for i in range(ls1+1)]
        
    for i in range(1,ls1+1):
        for j in range(1,ls2+1):
            if(s1[i-1]==s2[j-1]):
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i][j-1],l[i-1][j])
    i,j=ls1,ls2
    s=[]
    
    while(i!=0 or j!=0):
        if (s1[i-1]==s2[j-1]):
            s.append(s1[i-1])
            i=i-1
            j=j-1
        else:
            if (l[i][j]==l[i][j-1]):    
                j=j-1
            elif l[i][j]==l[i-1][j-1]+1:
                i=i-1
    return "".join(s[::-1])

s1=input()
print(lcs(s1,s1[::-1]))
