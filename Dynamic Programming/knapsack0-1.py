"""
Given weights and values of n items,
put these items in a knapsack of capacity W such that
the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""

total=7
weight=[1,3,4,5]
val=[1,4,5,7]

arr=[[0 for j in range((total+1))] for i in range(len(weight)+1)]

for i in range(1,len(weight)+1):
    for j in range(1,total+1):
        if j<weight[i-1]:
            arr[i][j]=arr[i-1][j]
        else:
            arr[i][j]=max(arr[i-1][j],arr[i-1][j-weight[i-1]]+val[i-1])

for i in arr:
    print(i)

print(arr[len(weight)][total])
