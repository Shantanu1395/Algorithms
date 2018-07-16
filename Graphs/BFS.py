class Vertex():
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjList = []

class BFS():
    def __init__(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:

            node = queue.pop(0)
            print(str(node.data),end = " ")

            for i in node.adjList:
                if not i.visited:
                    i.visited = True
                    queue.append(i)

if __name__ == '__main__':
    node0 = Vertex(0)
    node1 = Vertex(1)
    node2 = Vertex(2)
    node3 = Vertex(3)


    node0.adjList.append(node1)
    node0.adjList.append(node2)
    node1.adjList.append(node2)
    node2.adjList.append(node0)
    node2.adjList.append(node3)
    node3.adjList.append(node3)

    bfs = BFS(node2)