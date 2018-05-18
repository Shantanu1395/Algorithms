def isIsomorphic(str1,str2):
    mapping={}
    flag=True
    for i in range(len(str1)):
        if str1[i] in mapping:
            if not mapping[str1[i]]==str2[i]:
                flag=False
        else:
            mapping[str1[i]]=str2[i]
    return flag        
    
if __name__ == '__main__':
    str1=input()
    str2=input()
    print(isIsomorphic(str1,str2))
