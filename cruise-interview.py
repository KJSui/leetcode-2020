import collections
import heapq
class Solution:
    def bestTaskSequence(self, tasks, intervals):
        mp = collections.defaultdict(int)
        for i in tasks:
            mp[i] += 1
        pq = []
        res = []
        for i in (mp.keys()):
            tp = [-mp[i], i]
            heapq.heappush(pq, tp)
        while len(pq):
            length = intervals
            tmppq = []
            while length > 0 and len(pq):
                length -= 1
                tp = heapq.heappop(pq)
                res.append(tp[1])
                tp[0] += 1
                if tp[0] == 0:
                    continue
                tmppq.append(tp)
            while len(tmppq):
                heapq.heappush(pq, tmppq.pop(0))
        return res
obj = Solution()
tasks = ['1', '2', '3', '2', '1', '1', '4', '3', '3', '1']
intervals = 3
print(obj.bestTaskSequence(tasks, intervals))