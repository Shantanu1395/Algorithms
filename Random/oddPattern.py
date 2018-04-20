def printPattern(s):
    l=[]
    for i in range(len(s)//2):
        last=len(s)-i
        start=i
        l.append(" "*(i)+str(s[i])+(" "*(last-start-1))+str(s[len(s)-i-1]))
    print("\n".join(l))
    print((" "*(len(s)//2)) + str(s[len(s)//2]))
    print("\n".join(l[::-1]))
    

printPattern(input())
