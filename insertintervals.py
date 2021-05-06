# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        if len(intervals) == 0:
            return [newInterval]
        start = self.bsh(newInterval[0], 0, len(intervals)-1, intervals)
        i = start
        print("start:", start)
        if(i > 0):
            if intervals[i-1][1] >= newInterval[0]:
                newInterval[0] = intervals[i-1][0]
                newInterval[1] = max(intervals[i-1][1], newInterval[1])
                start -= 1
        
        while (i < len(intervals)):
            if newInterval[0] > intervals[i][1]:
                intervals.append(newInterval)
                return intervals            
            if newInterval[1] < intervals[i][0]:
                intervals = intervals[:start] + [newInterval] + intervals[i:]
                return intervals
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        intervals = intervals[:start] + [newInterval] + intervals[i:]
        return intervals

    def bsh(self, target, left, right, intervals):
        #print("target:", target, "left:", left, "right:", right, "intervals:", intervals)
        if left >= right:
            return left
        mid = left + int((right - left)/2)
        if intervals[mid][0] == target:
            return mid
        if target < intervals[mid][0]:
            return self.bsh(target, left, mid, intervals)
        else:
            return self.bsh(target, mid+1, right, intervals)
            