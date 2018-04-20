#Save a string in a matrix and search for a given string by printing their index

import math

def constructArray(s):
    side=int(math.ceil(math.sqrt(len(s))))
    arr=[]
    k=0
    for i in range(side):
        temp=[]
        for j in range(side):
            if k>=len(s):
                temp.append('_')
            else:
                temp.append(s[k])
                k+=1
        arr.append(temp)
    return arr

def stringSearch(arr,s):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i+1<len(arr) and i+2<len(arr)):
                if arr[i][j]=='T' and arr[i+1][j]=='O' and arr[i+2][j]=='O':
                    print(i,j)
                    print(i+2,j)
            if(j+1<len(arr) and j+2<len(arr)):
                if arr[i][j]=='T' and arr[i][j+1]=='O' and arr[i][j+2]=='O':
                    print(i,j)
                    print(i,j+2)        
                    

s="WELCOMETOZOHOCORPORATION"
arr=constructArray(s)
stringSearch(arr,"TOO")
