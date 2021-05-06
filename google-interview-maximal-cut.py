import collections
class Solution:
    def constructGraph(self, array):
        self.mp = collections.defaultdict(list)
        for i in range(len(array)):
            for j in range(len(array)):
                if j != i:
                    self.mp[i].append(j)
        print("mp:", self.mp)
    def checkGraphConnected(self, node):
        self.array = [False] * len(array)
        self.dfs(node)
        print("checked graph:", self.array)
        for j in self.array:
            if j is False:
                return True
        return False
    def dfs(self, idx):
        if self.array[idx] is True:
            return
        self.array[idx] = True
        for j in self.mp[idx]:
            self.dfs(j)
        return
    def getTwoSets(self, edges):
        gp1 = []
        gp2 = []
        edges = sorted(edges, reverse=True)
        print("edges:", edges)
        for edge in edges:
            if edge[2] in self.mp[edge[1]]:
                self.mp[edge[1]].remove(edge[2])
            if edge[1] in self.mp[edge[2]]:
                self.mp[edge[2]].remove(edge[1])
            print("cut mp:", self.mp, "edge[1]:", edge[1], "edge[2]:", edge[2])
            if self.checkGraphConnected(0):
                for i in range(len(self.array)):
                    if self.array[i] is True:
                        gp1.append(i)
                    else:
                        gp2.append(i)
                break
        return str(gp1) + ":" + str(gp2)

obj = Solution()
array = [0, 1, 2, 3]
edges = [[270, 0, 1], [60, 0, 2], [20, 0, 3], [35, 1, 2], [90, 1, 3], [100, 2, 3]]
obj.constructGraph(array)
print(obj.getTwoSets(edges))
        
        
