import collections
class Solution:
    def findShortestPathFromAllNodeTovisitedAllnode(self, edges):
        self.graph = collections.defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        self.len = len(self.graph.keys())
        self.res = float('inf')
        self.visited = set()
        for node in self.graph.keys():
            self.findPath(node, 0)
            self.visited = set()
        return self.res

    def findPath(self, node, depth):
        if len(self.visited) == self.len:
            self.res = min(self.res, depth)
            return
        if node not in self.graph:
            return
        if node in self.visited:
            return
        self.visited.add(node)
        for edge in self.graph[node]:
            depth += 1
            self.findPath(edge, depth)
        return

obj = Solution()
edges = [[0, 1], [0, 2], [0, 3]]
print(obj.findShortestPathFromAllNodeTovisitedAllnode(edges))
