class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}

        pq = [{0, 0, src}]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')):
                continue
            if place == dst:
                return cost
            
            for nei, wt in graph[place].iteritems():
                newcost = cost + wt
                if newcost < best.get((k+1, nei)):
                    best[k+1, nei] = newcost
                    heapq.heappush(pq, {newcost, k+1, nei})

        return -1
