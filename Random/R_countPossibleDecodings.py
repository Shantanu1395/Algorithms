#Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.
def calculateDecodings(s):
    count=[0]*(len(s)+1)
    count[0]=1
    count[1]=1
    for i in range(2,len(s)+1):
        if s[i-1]>'0':
            count[i]=count[i-1]
        if s[i-2]=='1' or (s[i-2]<='2' and s[i-1]<='6'):
            count[i]+=count[i-2]
    return count[len(s)]        
    
s=input()
print(calculateDecodings(s))
