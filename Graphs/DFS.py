class Vertex():
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjList = []

class DFSIterative():
    def __init__(self, startNode):
        stack = []
        stack.append(startNode)
        startNode.visited = True

        while stack:

            node = stack.pop(len(stack)-1)
            print(str(node.data),end = " ")

            for i in node.adjList:
                if not i.visited:
                    i.visited = True
                    stack.append(i)

class DFSRecursive():

    def dfs(self,node):
        node.visited = True
        print(node.data, end=" ")
        for i in node.adjList:
            if not i.visited:
                self.dfs(i)

if __name__ == '__main__':

    #Result in recursive and iterative versions would be same when items are inserted in reverse order in stack in iterative version

    node0, node1, node2, node3, node4 = Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4)
    node1.adjList.append(node0)
    node0.adjList.append(node2)
    node2.adjList.append(node1)
    node0.adjList.append(node3)
    node1.adjList.append(node4)
    dfs = DFSIterative(node0)
    print()

    node0, node1, node2, node3, node4 = Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4)
    node1.adjList.append(node0)
    node0.adjList.append(node2)
    node2.adjList.append(node1)
    node0.adjList.append(node3)
    node1.adjList.append(node4)
    dfs = DFSRecursive()
    dfs.dfs(node2)