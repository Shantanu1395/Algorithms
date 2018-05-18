#Ceasar Cipher

#input-ATTACKATONCE

inpt=list(input().lower())
shift=int(input())
for i in range(len(inpt)):
    #print(ord(inpt[i])-ord('a'))
    tempord=ord(inpt[i])-ord('a')+1
    if shift+tempord<=25:
        inpt[i]=chr(ord(inpt[i])+shift)
    else:
        secondhalf=(shift+tempord)-25
        #firsthalf=secondhalf-(shift+tempord)
        inpt[i]=chr(ord('a')+secondhalf-1)
        if secondhalf==1:
            inpt[i]='z'
        
print("".join(inpt))


#output-exxegoexsrgi
