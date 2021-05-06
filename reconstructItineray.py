class Solution:
    def findItinerary(self, tickets):
        hs = {}
        res = []
        for t in tickets:
            if t[0] not in hs:
                hs[t[0]] = [t[1]]
            else:
                hs[t[0]].append(t[1])

        for key in hs.keys():
            hs[key] = sorted(hs[key])

        def dfs(self, airport):
            while airport in hs and hs[airport]:
                dfs(hs[airport].pop(0))
            res.insert(0, airport)

        dfs("JFK")

        return res

        
