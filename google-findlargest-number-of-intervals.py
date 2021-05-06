#find the largest number of non-overlapping intervals
class Solution:
    def findNonOverlappingIntervals(self, intervals):
        intervals.sort(key = lambda x:x[0])
        res = i = idx = 0

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1
            res += 1
            #find the overlapping intervals min-start, min-end
            while i < len(intervals):
                if intervals[i][0] < end:
                    if intervals[i][1] < end:
                        idx = i
                    end = min(intervals[i][1], end)
                    i += 1
                else:
                    break
            
            #find next interval is non-overlapping with our previous min-end intervals
            i = idx + 1
            while i < len(intervals) and intervals[i][0] < end:
                i += 1
            if i >= len(intervals):
                return res
        
        return res


obj = Solution()
intervals = [[1, 4], [2, 4], [3, 5], [4, 5]]
print(obj.findNonOverlappingIntervals(intervals))
            

                
