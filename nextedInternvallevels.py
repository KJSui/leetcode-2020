import heapq
class Solution:
    def findLevelNestedList(self, intervals):
        intervals.sort(key = lambda x: x[0])
        res = 1
        i = 1
        lt = [intervals[0]]
        start = [intervals[0][0], intervals[0][1]]
        while i < len(intervals):
            print("start[0]: ", start[0], "interval:", intervals[i][0])
            if intervals[i][0] >= start[0] and intervals[i][1] <= start[1]:
                if len(lt) > 1:
                    if not (intervals[i][0] >= lt[-1][0] and intervals[i][1] <= lt[-1][0]):
                        res = max(res, len(lt))
                        lt = [intervals[i]]
                        start = i
                    else:
                        lt.append(intervals[i])
                        res = max(res, len(lt))
                else:
                    lt.append(intervals[i])
                    res = max(res, len(lt))
            else:
                res = max(res, len(lt))
                lt = [intervals[i]]
                start = i
            i += 1

intervals = [[1, 4], [2, 4], [3, 4], [3, 5]]
obj = Solution()
print(obj.findLevelNestedList(intervals))
                


