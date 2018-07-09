"""
#Problem
Given weights and values of n items,
put these items in a knapsack of capacity W such that
the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

To consider all subsets of items, there can be two cases for every item: (1) the item is included in the optimal subset, (2) not included in the optimal set.
Therefore, the maximum value that can be obtained from n items is max of following two values.
1) Maximum value obtained by n-1 items and W weight (excluding nth item).
2) Value of nth item plus maximum value obtained by n-1 items and W minus weight of the nth item (including nth item).

If weight of nth item is greater than W, then the nth item cannot be included and case 1 is the only possibility.
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
