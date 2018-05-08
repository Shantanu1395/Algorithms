count=0

def solve(maze,x1,y1,x2,y2):
    global count
    if x1>=len(maze) or y1>=len(maze):
        return False
    if maze[x1][y1]==0:
        return False
    if x1==x2 and y1==y2:
        maze[x1][y1]='*'
        count+=1
        return True
    maze[x1][y1]='*'
    return solve(maze,x1+1,y1,x2,y2) or solve(maze,x1,y1+1,x2,y2)



maze=[
    [1,0,0,0],
    [1,1,1,1],
    [0,1,0,0],
    [1,1,1,1]
    ]

for i in maze:
    print(i)

print(solve(maze,0,0,len(maze)-1,len(maze)-1))

for i in maze:
    print(i)

print(count)
