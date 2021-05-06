class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neigh = []

class Solution:
    def __init__(self):
        self.mp = defaultdict(set)
    def findAWay(self, N):
        for i in range(1, N+1):
            if self.directgraph(GraaphNode(i)):
                return True
        return False

    def directGraph(self, graphRoot):
        queue = [graphRoot]
        while queue:
            root = queue.pop(0)
            if root in self.mp.keys():
                continue
            for neigh in root.neigh:
                queue.append(neigh)
                self.mp[root.val].add(neigh.val)
                self.mp[graphRoot.val].add(neigh.val)
        if len(self.mp[graphRoot]) == N:
            return True
        return False
                

