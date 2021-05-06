from collections import defaultdict
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        mp = defaultdict(list)
        dmin = float('inf')
        dmax = 0
        for w in range(len(workers)):
            for b in range(len(bikes)):
                d = self.manhattan(workers[w], bikes[b])
                mp[d].append([w, b])
                if dmin > d:
                    dmin = d
                if dmax < d:
                    dmax = d
        print("dmin:", dmin, "dmax:", dmax)
        print("map:", mp)
        res = [-1] * len(workers)
        wset = set()
        bset = set()
        for i in range(dmin, dmax+1):
            if i in mp.keys():
                lt = mp[i]
                for j in lt:
                    if j[0] not in wset and j[1] not in bset:
                        res[j[0]] = j[1]
                        wset.add(j[0])
                        bset.add(j[1])
                        print("30line - distance:", i, "res: ", res)
        return res
                        
    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

obj = Solution()
workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]

print(obj.assignBikes(workers, bikes))