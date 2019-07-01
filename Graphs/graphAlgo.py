from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, fromNode, vertex):
        self.graph[fromNode].append(vertex)
        
    def __str__(self):
        for k,v in self.graph.items():
            print(str(k) + ":", end='')
            for i in v:
                print(i, end=' ')
            print()
        return ""   
        
    def bfs(self,start):
        queue = [start]
        visited = [start]
        while queue:
            if(len(queue)>0):
                top = queue.pop()
                print(top, end=' ')
                for i in self.graph[top]:
                    if i not in visited:
                        visited.append(i)
                        queue.insert(0, i)
graph = Graph()
graph.addEdge(0, 1) 
graph.addEdge(0, 2) 
graph.addEdge(1, 2) 
graph.addEdge(2, 0) 
graph.addEdge(2, 3) 
graph.addEdge(3, 3)
print(graph)
graph.bfs(2)


