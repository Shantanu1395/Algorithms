from collections import defaultdict
#graph = {'Cake':['cheeseCake', ice-cream cake', 'normal-cake']}


#       0 -1
#       | /
#       2 - 3
#
#   graph = {0:[1, 2], 1:[2], 2:[0, 3], 3:[3]}
#   visited = [False, False, False, False]

class Graph: 
  
    def __init__(self): 
  
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
  
    def BFS(self, s): 
  
        visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            s = queue.pop(0) 
            print (s, end = " ") 
  
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
    
    def DFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a stack for DFS 
        stack = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        stack.append(s) 
        visited[s] = True
  
        while stack: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = stack.pop(len(stack)-1)
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    stack.append(i) 
                    visited[i] = True
    
    def recursiveDFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
        self.recursiveDFSUtil(s, visited)
        
    def recursiveDFSUtil(self, s, visited):
        print(s, end=' ')
        visited[s] = True
        for i in self.graph[s]:    
            if(visited[i]==False):
                self.recursiveDFSUtil(i, visited)
            
  
# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 

print()
print ("Depth First Traversal"
                  " (starting from vertex 2)") 
g.DFS(2)
print()

g.recursiveDFS(2)
