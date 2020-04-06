#NOTE - 
# 1. Current code prints all nodes at all levels from a given node
# 2. Code can be modified to print nodes at level k => pass a parameter to bfs and break out of loop if level == k (Considering node itself is at level 1)
# 3. Code can be modified to print the time in which a tree burns if we apply fire on a node => return level from bfs

##############################
#Constructing the Tree
##############################
# Tree
#           26
#          / \
#         10  32
#        / \   \
#       4   6   3
#       \  
#       30

class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, data):
        self.data = data      
        self.right = None
        self.left = None

tree=Tree()
tree.root=Node(26)

tree.root.left=Node(10)
tree.root.right=Node(32)

tree.root.left.left=Node(4)
tree.root.left.right=Node(6)
tree.root.right.right=Node(3)

tree.root.left.left.right=Node(30)
##############################


##############################
#Constructing the dictionary(node -> parent) for parent look-up
##############################
dic = {}
def constructDict(root, parent, dic):
    if root:
        dic[root] = parent
        constructDict(root.left, root, dic)
        constructDict(root.right, root, dic)
constructDict(tree.root, None, dic)


##############################
#Utility Helper BFS
##############################
def bfs(root):
    q = []
    visited = set()
    visited.add(root)
    q.append(root)
    
    level = 0
    
    while q:
        nodesAtLevel = len(q)
        
        print(level)
        print([i.data for i in q])
        while nodesAtLevel > 0:
            node = q[0]
            if node.left and node.left not in  visited:
                q.append(node.left)
                visited.add(node.left)
            if node.right and node.right not in  visited:
                q.append(node.right)
                visited.add(node.right)
            if dic[node] is not None and dic[node] not in  visited:
                q.append(dic[node])
                visited.add(dic[node])
            q.pop(0)    
            nodesAtLevel -= 1
        level += 1    
    
    
##############################
#Function to find target node
##############################
def nodesAtKthDistance(root, target):
    if root:
        if root.data == target:
            bfs(root)
        nodesAtKthDistance(root.left, target)
        nodesAtKthDistance(root.right, target)    

##############################
#Runner function
##############################
if __name__ == "__main__":
    nodesAtKthDistance(tree.root, 10)
##############################
