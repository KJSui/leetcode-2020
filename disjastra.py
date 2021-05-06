class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]



class Solution:
    def minDistance(self, dist, sptset):
        min = sys.maxint
        for v in range(self.V):
            if dist[v] < min and sptset[v] == False:
                min = dist[v]
                min_index = v

    def dijkstra(self, src):
        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptset = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptset)
            sptset[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptset[v] == False and
                dist[v] > dist[u] + self.graph[u][v]:
                dist[v] = dist[u] + self.graph[u][v]

                
