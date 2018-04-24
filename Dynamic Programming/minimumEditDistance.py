def editdistance(s1,s2):
    ls1,ls2=len(s1),len(s2)
    
    l=[[0 for j in range(ls2+1)] for i in range(ls1+1)]
        
    for i in range(ls1+1):
        for j in range(ls2+1):
            if i==0:
                l[i][j]=j
            elif j==0:
                l[i][j]=i
            else:    
                if(s1[i-1]==s2[j-1]):
                    l[i][j]=l[i-1][j-1]
                else:
                    l[i][j]=min(l[i][j-1],l[i-1][j],l[i-1][j-1])+1
    return l[ls1][ls2]
        
        
s1=input()
s2=input()
print(editdistance(s1,s2))
