class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort()
        left = right = []
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 2
        i = 0
        j = 1
        res = set()
        while j < len(intervals):
            if intervals[i][1] <= intervals[j][0]:
                res.add(intervals[i][1])
                res.add(intervals[i][1]-1)
                res.add(intervals[j][0])
                res.add(intervals[j][0] + 1) 
                i = j
                j += 1
            else:
                intervals[i][0], intervals[i][1] = intervals[j][0], max(intervals[j][1], intervals[i][1])
                j += 1
            print("intervals:", intervals)
            print("result:", res)
        res.add(intervals[0][0]+1)
        res.add(intervals[0][0]+2)
        return len(res)
obj = Solution()
intervals = [[1,3],[1,4],[2,5],[3,5]]
print(obj.intersectionSizeTwo(intervals))