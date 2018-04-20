def checkCorrectness(arr):
    row=set()
    column=set()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]>0 and arr[i][j]<10:
                row.add(arr[i][j])
        for j in range(len(arr[i])):
            if arr[i][j]>0 and arr[i][j]<10:
                column.add(arr[j][i])        
    for i in range(1,10):
        if i not in (row or column):
            return False
    return True    

arr=[ [ 5, 1, 3, 6, 8, 7, 2, 4, 9 ], 
      [ 8, 4, 9, 5, 2, 1, 6, 3, 7 ],
      [ 2, 6, 7, 3, 4, 9, 5, 8, 1 ], 
      [ 1, 5, 8, 4, 6, 3, 9, 7, 2 ],
      [ 9, 7, 4, 2, 1, 8, 3, 6, 5 ], 
      [ 3, 2, 6, 7, 9, 5, 4, 1, 8 ],
      [ 7, 8, 2, 9, 3, 4, 1, 5, 6 ], 
      [ 6, 3, 5, 1, 7, 2, 8, 9, 4 ],
      [ 4, 9, 1, 8, 5, 6, 7, 2, 3 ]
      ]

print("Correct" if checkCorrectness(arr) else "Incorrect")
