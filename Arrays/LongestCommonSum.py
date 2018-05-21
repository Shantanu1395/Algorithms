#Longest Span with same Sum in two Binary arrays
def longestCommonSum(arr1,arr2):
    maximum=0
    for i in range(len(arr1)):
        sum1,sum2=0,0
        for j in range(i,len(arr2)):
            sum1+=arr1[j]
            sum2+=arr2[j]

            if sum1==sum2:
                if j-i+1>maximum:
                    maximum=j-i+1
    return maximum                
                
arr1=[0,1,0,0,0,0]
arr2=[1,0,1,0,0,1]

print(longestCommonSum(arr1,arr2))
