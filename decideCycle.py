from collections import defaultdict

class  Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True 

        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, visited, recStack):
                    return True 
                elif recStack[neighbor] == True:
                    return True 

        recStack[v] = False 
        return False 

    def isCyclic(self):
        visited= [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack):
                    return True 

        return False 


##################
#################
####union find method to find a cycle
def find_parent(self, parent, i):
    if parent[i] == -1:
        return i   
    if parent[i] != i:
        return self.find_parent(parent, parent[i])

def union(self, parent, x, y):
    x_set = self.find_parent(parent, x)
    y_set = self.find_parent(parent, y)
    parent[x_set] = y_set


def isCyclic(self):
    parent = [-1]*self.V  

    for i in self.graph:
        for j in self.graph[i]:
            x = self.find_parent(parent, i)
            y = self.find_parent(parent, j)
            if x == y:
                return True 
            self.union(parent, x, y)

            