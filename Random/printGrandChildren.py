def printGrandChildren(arr,s):
    l1=[]
    l2=[]
    for i in arr:
        l1.append(i[0])
        l2.append(i[1])
        
    if s in l2:
        children=l1[l2.index(s)]
        for i in range(len(l2)):
            if l2[i]==children:
                print(l1[i])

arr=[
    ["luke","shaw"],
    ["wayne","rooney"],
    ["rooney","ronaldo"],
    ["shaw","rooney"]
    ]

printGrandChildren(arr,input())
