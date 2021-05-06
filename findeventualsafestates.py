import collections
class Solution:
    def eventualSafeNodes(self, graph):
        self.mp = collections.defaultdict(list)
        self.safe = {}
        self.res = []
        self.visited = set()
        for i, edge in enumerate(graph):
            if len(edge) == 0:
                self.safe[i] = True
                continue
            self.mp[i] += edge
        print("map:", self.mp)
        print("safe:", self.safe)
        for i in range(len(graph)):
            if i in self.safe:
                if self.safe[i] == True and i not in self.res:
                    self.res.append(i)
                continue
            if self.dfs(i):
                self.res.append(i)
        
        return self.res
            
    
    def dfs(self, node):
        print("node:", node)
        if node not in self.mp.keys():
            self.safe[node] = True
            return True
        if node in self.visited:
            return False
        self.visited.add(node)
        if node in self.safe.keys():
            return self.safe[node]
        lt = self.mp[node]
        print("curr node directed lines:", lt)
        
        self.safe[node] = True 
        for v in lt:
            if self.dfs(v) == False:
                self.safe[node] = False
                return False
            
        return True
        
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
obj = Solution()
print(obj.eventualSafeNodes(graph))