#Remove all characters from s1 present in s2

s1=list(input())
s2=list(input())

i1,i2=0,0
s=""

while True:
    if i1==len(s1) or i2==len(s2):
        break
    if s2[i2]==s1[i1]:
        i1+=1
        i2+=1
    else:
        s+=s1[i1]
        i1+=1

print(s)        
