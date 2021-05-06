"""
Give two companies and a graph, output the total weight company A to B.
A own 40% of B
B own 40% of C
A own 5% of C

Total = 40% * 40% + 5%
"""
import collections
class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def gettotalweight(self, graph, c1, c2):
        for edge in graph:
            self.graph[edge[0]].append(edge[1:])
        self.total = 0
        self.dfs(c1, c2, 1)
        return self.total
        
    def dfs(self, c1, c2, pathsum):
        if c1 == c2:
            self.total += pathsum * 100
            return
        if c1 not in self.graph:
            return
        lt = self.graph[c1]
        for i in lt:
            self.dfs(i[0], c2, pathsum * float(i[1])/100)
        return

obj = Solution()
graph = [['a', 'b', 30], ['b', 'c', 40], ['a', 'c', 5]]
c1 = 'a'
c2 = 'c'
print(obj.gettotalweight(graph, c1, c2))